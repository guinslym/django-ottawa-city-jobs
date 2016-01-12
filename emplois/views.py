from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.conf import settings    

#Task queues
from django_q.tasks import async, schedule, result
from django_q.models import Schedule

from django.views.decorators.cache import cache_page

from .models import Job, Description
from .utils import job_object_list, language_set
# Create your views here.

class IndexView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'
    

    def get_queryset(self):
       #print(self.request.LANGUAGE_CODE) #'en-us
       language = language_set(self.request.LANGUAGE_CODE)
       #import ipdb;ipdb.set_trace()
       #tid = async('subprocess.run', ['cp', 'setup.py', 'setup.py.bak'])
       #job_object_list()
       return Job.objects.filter(language=language, 
        expirydate__gt=datetime.now())\
            .order_by('expirydate')

class LatestView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       language = language_set(self.request.LANGUAGE_CODE)
       return Job.objects.filter(language=language, 
        pub_date__gte=datetime.now()-timedelta(days=14)).order_by('expirydate')

class ExpiringSoonView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       language = language_set(self.request.LANGUAGE_CODE)
       return Job.objects.filter(language=language, 
        expirydate__lte=datetime.now()+timedelta(days=14)).order_by('expirydate')

class AllJobsView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       language = language_set(self.request.LANGUAGE_CODE)
       return Job.objects.filter(language=language).order_by('expirydate')

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


class AboutView(generic.TemplateView):
    template_name='emplois/about.html'
    #context_object_name='latest_jobs_list'


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

   