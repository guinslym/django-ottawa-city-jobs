from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Job, Description
# Create your views here.

class IndexView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.order_by('-pub_date')

class LatestView(generic.ListView):
    template_name='emplois/latest.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.order_by('-pub_date')

class SalaryView(generic.ListView):
    template_name='emplois/salary.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.order_by('-salarymax')

class ExpiringSoonView(generic.ListView):
    template_name='emplois/expire.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.order_by('-expirydate')

class DetailView(generic.DetailView):
    model = Job
    template_name = 'emplois/details.html'
    context_object_name='job'

class StatsView(generic.TemplateView):
    template_name='emplois/stats.html'
    #context_object_name='latest_jobs_list'
    def get_contet_data(self, **kwargs):
        import time
        import dateutil.parser
        import datetime
        """

        """
        context = super(StatsView, self).get_context_data(**kwargs)
        #get all the English values
        english = Job.objects.filter(language='EN')
        #Grouup by date
        context['stats'] = english.values('pub_date').annotate(dcount=Count('pub_date'))
        return context


class AboutView(generic.TemplateView):
    template_name='emplois/about.html'
    #context_object_name='latest_jobs_list'
