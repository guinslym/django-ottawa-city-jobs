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
            (FRENCH, 'Francais'),
            (ENGLISH, 'English'),
            )
    def __str__(self):
        return self.POSITION
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.POSTDATE <= now
    def still_not_expired_job_list(self):
        now = timezone.now()
        return self.EXPIRYDATE >= now


    JOBURL = models.URLField(max_length=250, blank=True, null=True)
    EXPIRYDATE = models.DateField(auto_now=False, blank=True, null=True)
    SALARYMAX = models.CharField(max_length=40, blank=True, null=True)
    SALARYMIN = models.CharField(max_length=40, blank=True, null=True)
    SALARYTYPE = models.CharField(max_length=20, blank=True, null=True)
    NAME = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, default=ENGLISH)
    POSITION = models.CharField(max_length=150, blank=True, null=True)
    JOBREF = models.CharField(max_length=30, unique=True, blank=True, null=True)
    JOB_SUMMARY = models.TextField(blank=True, null=True)
    POSTDATE = models.DateTimeField(auto_now=False, blank=True, null=True)
    slug = models.CharField(max_length=200)
    tweeted = models.BooleanField(default=False)

@python_2_unicode_compatible
class Description(models.Model):
    '''
    Job.Description.models
    '''
    def __str__(self):
        return self.COMPANY_DESC

    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    KNOWLEDGE = models.TextField(blank=True, null=True)
    LANGUAGE_CERTIFICATES = models.TextField(blank=True, null=True)
    EDUCATIONANDEXP = models.TextField(blank=True, null=True)
    COMPANY_DESC = models.TextField(blank=True, null=True)
    POSTDATE = models.DateTimeField(auto_now=True, blank=True, null=True)
