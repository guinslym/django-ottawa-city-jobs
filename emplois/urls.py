#!/usr/bin python3
# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views import generic
__author__ = 'Guinsly'

app_name = 'emplois'
urlpatterns = [
      url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
      url(r'^stats$', views.StatsView.as_view(), name='stats'),
      url(r'^searchJobs/$', views.job_search, name='job_search'),
      url(r'^emplois/$', views.emplois, name='emplois'),
      url(r'^about$', views.AboutView.as_view(), name='about'),
      url(r'^all_jobs_posted$', views.AllJobsView.as_view(), name='all_jobs_posted'),
      url(r'^expiring$', views.ExpiringSoonView.as_view(), name='expire'),
      url(r'^latest$', views.LatestView.as_view(), name='latest'),
      url(r'^i18n/', include('django.conf.urls.i18n')),
      #url(r'^(?P<lang>\w+)/$', generic.RedirectView.as_view(), name='lang_redirect'),
      url(r'^$', views.IndexView.as_view(), name='index'),

        ]
