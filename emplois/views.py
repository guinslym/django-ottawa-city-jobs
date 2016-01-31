from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.conf import settings 
#pagination   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Task queues
from django_q.tasks import async, schedule, result
from django_q.models import Schedule
#cache
from django.views.decorators.cache import cache_page
#models and utils
from .models import Job, Description
from .utils import job_object_list, language_set
# Create your views here.

#http:://localhost:8001/
class IndexView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'
    paginate_by = 10
    

    def get_queryset(self):
       #print(self.request.LANGUAGE_CODE) #'en-us
       language = language_set(self.request.LANGUAGE_CODE)
       #import ipdb;ipdb.set_trace()
       return Job.objects.filter(language=language, 
        expirydate__gt=datetime.now())\
            .order_by('expirydate')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) 
        language = language_set(self.request.LANGUAGE_CODE)
        latest_jobs_list = Job.objects.filter(language=language, 
                            expirydate__gt=datetime.now())\
                        .order_by('expirydate')
        paginator = Paginator(latest_jobs_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            latest_jobs_list = paginator.page(page)
        except PageNotAnInteger:
            latest_jobs_list = paginator.page(1)
        except EmptyPage:
            latest_jobs_list = paginator.page(paginator.num_pages)

        context['latest_jobs_list'] = latest_jobs_list
        return context

#http://localhost:8001/emplois/latest
class LatestView(generic.ListView):
    template_name='emplois/index.html'
    paginate_by = 10 
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       language = language_set(self.request.LANGUAGE_CODE)
       return Job.objects.filter(language=language, 
        pub_date__gte=datetime.now()-timedelta(days=14)).order_by('expirydate')


#http://localhost:8001/emplois/expiring
class ExpiringSoonView(generic.ListView):
    template_name='emplois/index.html'
    paginate_by = 10 
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       language = language_set(self.request.LANGUAGE_CODE)
       return Job.objects.filter(language=language, 
        expirydate__lte=datetime.now()+timedelta(days=14)).order_by('expirydate')

#http://localhost:8001/emplois/all_job_posted
class AllJobsView(generic.ListView):
    template_name='emplois/index.html'
    paginate_by = 10 
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       language = language_set(self.request.LANGUAGE_CODE)
       return Job.objects.filter(language=language).order_by('expirydate')

#http://localhost:8001/emplois/<id>
class DetailView(generic.DetailView):
    model = Job
    paginate_by = 10 
    template_name = 'emplois/details.html'
    context_object_name='job'

#http://localhost:8001/emplois/stats
class StatsView(generic.TemplateView):
    template_name='emplois/stats.html'
    #context_object_name='latest_jobs_list'
    paginate_by = 10 
    def get_context_data(self, **kwargs):
        """

        """
        import time
        from django.db.models import Count
        #
        context = super(StatsView, self).get_context_data(**kwargs)
        #get all the English values
        language = language_set(self.request.LANGUAGE_CODE)
        english = Job.objects.filter(language=language)
        #Grouup by date
        data = english.values('pub_date').annotate(dcount=Count('pub_date'))
        content = {}
        for job in data:
            unix_time = time.mktime(job['pub_date'].timetuple())
            content.update({unix_time:job['dcount']})
        context['stats'] = content

        return context

#http://localhost:8001/emplois/about
class AboutView(generic.TemplateView):
    template_name='emplois/about.html'
    context_object_name='language'

    def get_context_data(self, **kwargs):
        """

        """
        import time
        from django.db.models import Count
        #
        context = super(AboutView, self).get_context_data(**kwargs)
        context['language'] = language_set(self.request.LANGUAGE_CODE)

        return context

#http://localhost:8001/emplois/searchJobs/<searchKey>
@cache_page(60 * 1, key_prefix="site1"  )
def job_search(request):
    if 'searchKey' in request.GET:
        keyword = request.GET['searchKey']
        if not keyword :
                return redirect('/')
        else:
            lang = language_set(request.LANGUAGE_CODE)
            latest_jobs_list = Job.objects.filter(position__icontains = keyword,language__icontains=lang).order_by('-pub_date')
            paginator = Paginator(latest_jobs_list, 10)
            page = request.GET.get('page')
            try:
                latest_jobs_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                latest_jobs_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                latest_jobs_list = paginator.page(paginator.num_pages)
            return render(request,'emplois/result.html',{'latest_jobs_list':latest_jobs_list})
    return redirect('/')

##########JAVASCRIPT = JSOM ##########
#http://localhost:8001/emplois/<annee>/<mois>/<jour>
def emplois(request):
    import datetime
    foos = Job.objects.filter(
        pub_date__year=request.GET.get('annee'),
        pub_date__month=request.GET.get('mois'),
        pub_date__day=request.GET.get('jour'),
        language=language_set(request.LANGUAGE_CODE)
        )
    data = serializers.serialize('json', foos)
    return HttpResponse(data, content_type='application/json')



##########TWITTER + Update the content######################
def update_and_tweets(request):
    from datetime import datetime, timedelta, time
    from pytz import timezone
    ottawa_timezone = timezone('America/Montreal')
    ottawa_now = datetime.now(ottawa_timezone)
    now_time = ottawa_now.time()
    tweet_time = now_time #>= time(5,30) #and now_time <= time(18,30)
    upgrade_time = (now_time >= time(12,00) and now_time <= time(16,30))
    if tweet_time:
        #tweet
        from .tweets import tweet_a_job
        tweet_a_job()
        print('Tweet time')
        return HttpResponse("<h1>Tweet time </h1>")
    elif upgrade_time: 
        #Update the list of jobs from Open Data portal (Ottawa.open.data)
        print('Upgrade time')
        #job_object_list()
        return HttpResponse("<h1>Upgrade time</h1>")
    else:
        print('nothing')
        return HttpResponse("<h1>Nothing</h1>")

#Error on this template
#I try  to create a Class based view of 'def job_search()'
class SearchJobView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get(self, request, *args, **kwargs):
        response = super(self, SearchJobView).get(request, *args, **kwargs)
        keyword = kwargs.get('searchKey')
        if keyword:
            return Job.objects.filter(position__icontains = keyword).order_by('-pub_date')
        else:
            return redirect('/')

   
