# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone


# Create your models here.
@python_2_unicode_compatible
class Job(models.Model):
    '''
    Job.models
    '''
    FRENCH = 'FR'
    ENGLISH = 'EN'
    LANGUAGE_CHOICE = (
            (FRENCH, 'FR'),
            (ENGLISH, 'EN'),
            )
    company_desc = models.TextField(blank=True, null=True)
    educationandexp = models.TextField(blank=True, null=True)
    expirydate = models.DateTimeField(auto_now=False, blank=True, null=True)
    joburl = models.URLField(max_length=250, blank=True, null=True)
    jobref = models.CharField(max_length=30, unique=True, blank=True, null=True)
    job_summary = models.TextField(blank=True, null=True)
    knowledge = models.TextField(blank=True, null=True)
    language_certificates = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, default=ENGLISH) 
    name = models.URLField(max_length=250, blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    postdate = models.DateTimeField(auto_now=False, blank=True, null=True)
    salarymin = models.CharField(max_length=40, blank=True, null=True)
    salarymax = models.CharField(max_length=40, blank=True, null=True)
    salarytype = models.CharField(max_length=20, blank=True, null=True)
    tweeted = models.BooleanField(default=False)
    slug = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.position
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.postdate <= now
    def still_not_expired_job_list(self):
        now = timezone.now()
        return self.expirydate >= now 



class Description(models.Model):
    '''
    Job.Description.models
    '''
    def __str__(self):
        return self.company_desc

    company_desc = models.TextField(blank=True, null=True)
    postdate = models.DateTimeField(auto_now=False, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True, blank=True, null=True)

"""

@python_2_unicode_compatible
class Description(models.Model):
    '''
    Job.Description.models
    '''
    def __str__(self):
        return self.company_desc

    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    knowledge = models.TextField(blank=True, null=True)
    languagecert = models.TextField(blank=True, null=True)
    educationandexp = models.TextField(blank=True, null=True)
    company_desc = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True, blank=True, null=True)




import json
from dateutil.parser import parse

#indentation error
def open_json()
    with open('a.json') as data_file:
        data = json.load(data_file)
    return data

data = data['jobs']

for i in data:
    p = i.get('POSTDATE')
    p = parse(p)
    p = p.strftime('%Y-%m-%d')
    Description.objects.create(postdate=p)

"""

