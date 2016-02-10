# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views import generic
from django.views.decorators.cache import cache_page
__author__ = 'Guinsly'

app_name = 'emplois'
urlpatterns = [
      url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
      url(r'^stats$', views.StatsView.as_view(), name='stats'),
      url(r'^searchJobs/$', cache_page(60 * 15)(views.job_search), name='job_search'),
      url(r'^stats_emplois/$', views.emplois, name='emplois'),
      url(r'^about$', views.AboutView.as_view(), name='about'),
      url(r'^all_jobs_posted$', views.AllJobsView.as_view(), name='all_jobs_posted'),
      url(r'^expiring$', views.ExpiringSoonView.as_view(), name='expire'),
      url(r'^latest$', views.LatestView.as_view(), name='latest'),
      url(r'^i18n/', include('django.conf.urls.i18n')),
      url(r'^update/$', views.update_and_tweets, name='upgrade'),
      url(r'^download/$', views.download, name='download'),
      #url(r'^(?P<lang>\w+)/$', generic.RedirectView.as_view(), name='lang_redirect'),
      url(r'^emplois/$', views.IndexView.as_view(), name='index'),
      url(r'^$', views.IndexView.as_view(), name='index'),

        ]
 