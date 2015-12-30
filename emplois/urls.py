from django.conf.urls import url

from . import views

app_name = 'emplois'
urlpatterns = [
      url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
      url(r'^salary$', views.SalaryView.as_view(), name='salary'),
      url(r'^expiring$', views.ExpiringSoonView.as_view(), name='expire'),
      url(r'^latest$', views.LatestView.as_view(), name='latest'),
      url(r'^$', views.IndexView.as_view(), name='index'),

        ]
