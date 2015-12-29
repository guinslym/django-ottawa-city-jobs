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

def mainpage():
	print('hello')