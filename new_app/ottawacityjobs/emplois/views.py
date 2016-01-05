from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Job, Description
# Create your views here.

class IndexView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       print(self.request.LANGUAGE_CODE)
       return Job.objects.filter(language='EN').order_by('-pub_date')

class LatestView(generic.ListView):
    template_name='emplois/index.html'
    context_object_name='latest_jobs_list'

    def get_queryset(self):
       return Job.objects.order_by('-pub_date')

class ExpiringSoonView(generic.ListView):
    template_name='emplois/index.html'
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
    def get_context_data(self, **kwargs):
        """

        """
        import dateutil.parser
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
def blog_search(request):
    if 'searchKey' in request.GET:
        keyword = request.GET['searchKey']
        if not keyword :
                return render(request,'emplois/index.html',{'error':True})
        else:
            latest_jobs_list = Job.objects.filter(position__icontains = keyword).order_by('-pub_date')
            if latest_jobs_list.count()==0 :
                return render(request,'emplois/index.html',{'latest_jobs_list':latest_jobs_list,'error':True, 'keyword': keyword})
            else:
                return render(request,'emplois/index.html',{'latest_jobs_list':latest_jobs_list,'error':False, 'keyword': keyword})
    return redirect('/')



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
            return None


from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

from django.utils.translation import pgettext

verbe = pgettext("verbe 'avoir'", "as")
valeur = pgettext("carte de jeu", "as")
carte = _("%(suj)s %(ver)s : %(val)s %(col)s") % {
    "suj": _("tu"), 
    "ver": verbe,
    "val": valeur, 
    "col": _("de trèfle")}
    
def test_i18n(request):
    nb_chats = 2
    couleur = "blanc"
    chaine = _("J'ai un %(animal)s %(col)s.") % {'animal': 'chat', 'col': couleur}
    infos = ungettext(
        "… et selon mes informations, vous avez %(nb)s chat %(col)s !",
        "… et selon mes informations, vous avez %(nb)s chats %(col)ss !",
        nb_chats) % {'nb': nb_chats, 'col': couleur}

    return render(request, 'test_i18n.html', locals())