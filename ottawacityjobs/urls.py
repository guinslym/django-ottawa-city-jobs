"""ottawacityjobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

#from applications.cityjobs.views import *

urlpatterns = [
    url(r'^jobs/', all_jobs),
    #url(r'^desc/', all_descriptions),
    url(r'^emplois/', include('applications.emplois.urls', namespace="emplois")),
    url(r'^ottawacityjobs/', include('applications.emplois.urls')),
    url(r'^admin/', admin.site.urls),
    # i18n
    url(r'^i18n/', include('django.conf.urls.i18n')),
    #url (r'^settings', include('metasettings.urls')),
    #url(r'^searchBlog/$','emplois.views.SearchJobView',name="blog_search"),
    url(r'^', include('applications.emplois.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'applications.emplois.views.handler404'
handler500 = 'applications.emplois.views.handler500'
