from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from datetime import datetime, timedelta

#Task queues
from django_q.tasks import async, schedule, result
from django_q.models import Schedule

from django.views.decorators.cache import cache_page

from .models import Job, Description
from .utils import job_object_list, hello
# Create your views here.

class IndexView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       #print(self.request.LANGUAGE_CODE) #'en-us
       tid = async('subprocess.run', ['cp', 'setup.py', 'setup.py.bak'])
       #job_object_list()
       return Job.objects.filter(language='EN', 
        expirydate__gt=datetime.now())\
            .order_by('expirydate')

class LatestView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.filter(language='EN', 
        pub_date__gte=datetime.now()-timedelta(days=14)).order_by('expirydate')

class ExpiringSoonView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.filter(language='EN', 
        expirydate__lte=datetime.now()+timedelta(days=14)).order_by('expirydate')

class AllJobsView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.filter(language='EN').order_by('expirydate')

class DetailView(generic.DetailView):
    model = Job
    template_name = 'emplois/details.html'
    context_object_name='job'

class StatsView(generic.TemplateView):
    template_name='emplois/stats.html'
    #context_object_name='latest_jobs_list'
    def get_context_data(self, **kwargs):
        """

        """
        import time
        from django.db.models import Count
        #
        context = super(StatsView, self).get_context_data(**kwargs)
        #get all the English values
        english = Job.objects.filter(language='EN')
        #Grouup by date
        data = english.values('pub_date').annotate(dcount=Count('pub_date'))
        content = {}
        for job in data:
            unix_time = time.mktime(job['pub_date'].timetuple())
            content.update({unix_time:job['dcount']})
        context['stats'] = content

        return context


class AboutView(generic.TemplateView):
    template_name='emplois/about.html'
    #context_object_name='latest_jobs_list'



class SetLanguageView(generic.RedirectView):
    #url = reverse('index')

    def get(self, request, *args, **kwargs):
        response = super(self, SetLanguageView).get(request, *args, **kwargs)
        lang = kwargs.get('lang')
        if lang:
            # To set the language for this session
            request.session[settings.LANGUAGE_SESSION_KEY] = lang
            # To set it as a cookie
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang,
                            max_age=settings.LANGUAGE_COOKIE_AGE,
                            path=settings.LANGUAGE_COOKIE_PATH,
                            domain=settings.LANGUAGE_COOKIE_DOMAIN)
        return response
#https://stackoverflow.com/questions/32258010/django-i18n-particular-behavior-setup

#https://github.com/roadrui/ruiblog/blob/master/ruiblog/views.py
@cache_page(60 * 1, key_prefix="site1"  )
def job_search(request):
    if 'searchKey' in request.GET:
        keyword = request.GET['searchKey']
        if not keyword :
                return redirect('/')
        else:
            latest_jobs_list = Job.objects.filter(position__icontains = keyword,language__icontains='EN').order_by('-pub_date')
            return render(request,'emplois/index.html',{'latest_jobs_list':latest_jobs_list,'error':False, 'keyword': keyword})
    return redirect('/')

##########outside##########
def emplois(request):
    foos = Job.objects.all()
    data = serializers.serialize('json', foos)
    return HttpResponse(data, mimetype='application/json')


#Error on this template
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

   