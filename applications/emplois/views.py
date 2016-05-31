# -*- coding: utf-8 -*-
#Django
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings
#pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Task queues
#cache
from django.views.decorators.cache import cache_page
#models and utils
from .models import Job, Description
#from .utils import job_object_list, language_set
# Standard Python module
from json import dumps, loads
from datetime import datetime, timedelta
# Create your views here.

from django.http import HttpResponseRedirect
from .utils import process_it

import logging
logger = logging.getLogger(__name__)

def language_set(language):
    if "-" in language:
        return (language.split('-')[1]).upper()
    else:
        return language.upper()

def hello(request):
  return HttpResponse('<h1>Hello world emplois 2</h1>')


#http:://localhost:8001/
class IndexView(generic.ListView):
    """
    this is the ROOT page
    return a list of Jobs
    """
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'
    paginate_by = 10

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        language = language.upper()
        return language

    def get_queryset(self):
        """
        Return a list of Jobs that have an EXPIRATION DATE
        greater than Now() and a default Language
        """
        #import ipdb;ipdb.set_trace()
        return Job.objects.filter(language=self.language(),\
              EXPIRYDATE__gt=datetime.now())\
            .order_by('EXPIRYDATE')


#http://localhost:8001/emplois/latest
class LatestView(generic.ListView):
    """Retrieve the latest jobs that Ottawa had
    published these past 2 weeks
    """
    template_name='emplois/index.html'
    paginate_by = 10
    context_object_name='latest_jobs_list'

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

    def get_queryset(self):
        """
        Return a list of Jobs that has a PUBLICATION DATE
        within the past 2 weeks

        Order: by PUBLICATION DATE
        """
        return Job.objects.filter(language=self.language(),
        POSTDATE__gte=datetime.now()-timedelta(days=14)).order_by('-POSTDATE')


#http://localhost:8001/emplois/expiring
class ExpiringSoonView(generic.ListView):
    """
    return a list of Jobs that will expire within the next two weeks
    """
    template_name='emplois/index.html'
    paginate_by = 10
    context_object_name='latest_jobs_list'

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

    def get_queryset(self):
        """
        Return a list of jobs
        that expires within today's Date and 2 weeks
        from now

        Order_by = Expiration Date
        """
        today =  timezone.now().date()
        ending_in_two_weeks = datetime.now()+timedelta(days=14)
        return Job.objects.filter(language=self.language(),
         EXPIRYDATE__lte=ending_in_two_weeks,EXPIRYDATE__gte=today)\
                 .order_by('EXPIRYDATE')

#http://localhost:8001/emplois/all_job_posted
class AllJobsView(generic.ListView):
    """
    Return all Jobs that are in the Database
    """
    template_name='emplois/index.html'
    paginate_by = 10
    context_object_name='latest_jobs_list'

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

    def get_queryset(self):
        """Return all the Jobs

        order by: PUBLICATION DATE
        latest is at the end
        """
        return Job.objects.filter(language=self.language()).order_by('POSTDATE')

#http://localhost:8001/emplois/<id>
class DetailView(generic.DetailView):
    """
    Return the detail content of a job

    NOTES???: The language is set by default
    """
    model = Job
    paginate_by = 10
    template_name = 'emplois/details.html'
    context_object_name='job'

#http://localhost:8001/emplois/stats
class StatsView(generic.TemplateView):
    """
    Return a list of aggratated timestamps that will populate
    the Javascript array in order to make the
    Calendar HeatMap view
    """
    template_name='emplois/stats.html'

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

    def get_context_data(self, **kwargs):
        """
        Return a list of Job's date
        """
        import time
        from django.db.models import Count
        #
        context = super(StatsView, self).get_context_data(**kwargs)
        #get all the English/French values
        english = Job.objects.filter(language=self.language())
        #Grouup by date
        data = english.values('POSTDATE').annotate(dcount=Count('POSTDATE'))
        content = {}
        #I want the date in a UNIX TIME format
        for job in data:
            unix_time = time.mktime(job['POSTDATE'].timetuple())
            content.update({unix_time:job['dcount']})
        context['stats'] = content

        return context

#http://localhost:8001/emplois/about
class AboutView(generic.TemplateView):
    """Retuns a static page that
    will show why do I create this website
    """
    template_name='emplois/about.html'
    context_object_name='language'

    def get_context_data(self, **kwargs):
        """
        Returns the language value
        """
        context = super(AboutView, self).get_context_data(**kwargs)
        context['language'] = language_set(self.request.LANGUAGE_CODE)

        return context

#http://localhost:8001/emplois/searchJobs/<searchKey>
#@cache_page(60 * 1, key_prefix="site1"  )
def job_search(request):
    """
    This function will receive a query
    from the Search Box and will return a list of
    jobs from that query
    """
    if 'searchKey' in request.GET:
        keyword = request.GET['searchKey']
        if not keyword :
                return redirect('/')
        else:
            lang = language_set(request.LANGUAGE_CODE)
            latest_jobs_list = Job.objects.filter(POSITION__icontains\
                    = keyword,language__icontains=lang).\
                    order_by('-POSTDATE')
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
    """
    This will receive an AJAX request and will return a JSON
    object
    """
    import datetime
    jobs = Job.objects.filter(
        POSTDATE__year=request.GET.get('annee'),
        POSTDATE__month=request.GET.get('mois'),
        POSTDATE__day=request.GET.get('jour'),
        language=language_set(request.LANGUAGE_CODE)
        )
    logger.info('Annee : ' + request.GET.get('annee') )
    logger.info('Mois : ' + request.GET.get('mois'))
    logger.info('Jour : ' + request.GET.get('jour'))
    logger.info('Language Code : ' + request.LANGUAGE_CODE)
    data = serializers.serialize('json', jobs)
    return HttpResponse(data, content_type='application/json')

#http://localhost:8001/emplois/download
def download(request):
    """
    This will return all the Job objects form the DB
    in JSON
    """
    import datetime
    data = serializers.serialize('json', Job.objects.all() )
    data = dumps(loads(data), indent=4)
    return HttpResponse(data, content_type='application/json')



def update_and_tweets(request):
    """
    This will update or tweet
    depending on the time
    """
    logger.info('Updating the list of jobs')
    from datetime import datetime, timedelta, time
    from pytz import timezone

    ottawa_timezone = timezone('America/Montreal')
    ottawa_now = datetime.now(ottawa_timezone)
    now_time = ottawa_now.time()
    #tweet_time = False#now_time >= time(5,30) and now_time <= time(18,30)
    upgrade_time = True# now_time >= time(17,00) and now_time <= time(19,30)

    if upgrade_time:
        res = process_it()
        #Update the list of jobs from Open Data portal (Ottawa.open.data)
        logger.infor('yes we add new jobs')
        return redirect("/")
    else:
        logger.info('no we didn t have new jobs in full.json')
        return redirect("/")


#Error on this template
#I try  to create a Class based view of 'def job_search()'
class SearchJobView(generic.ListView):
    """
    An attempt to use a Class Based view to
    process the job search
    """
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get(self, request, *args, **kwargs):
        response = super(self, SearchJobView).get(request, *args, **kwargs)
        keyword = kwargs.get('searchKey')
        if keyword:
            return Job.objects.filter(POSITION__icontains = keyword).order_by('-POSTDATE')
        else:
            return redirect('/')

def handler404(request):
    response = render(request, 'emplois/page_not_found.html')
    logger.info('Error page not found 404')
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, 'emplois/server_error.html')
    logger.info('Error page not found 500')
    response.status_code = 500
    return response

