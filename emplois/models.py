from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Job(models.Model):
    '''

    '''
    def __str__(self):
        return self.position
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now
    def still_not_expired_job_list(self):
        now = timezone.now()
        return self.expirydate >= now 


    joburl = models.URLField(max_length=250, blank=True, null=True)
    expirydate = models.DateField(blank=True, null=True)
    salarymax = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True) 
    position = models.CharField(max_length=150, blank=True, null=True)
    jobref = models.CharField(max_length=30, unique=True, blank=True, null=True)
    job_summary = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    timestamps = models.DateTimeField(auto_now=True, blank=True, null=True)

@python_2_unicode_compatible
class Description(models.Model):
    '''

    '''
    def __str__(self):
        return self.company_desc

    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    salarytype = models.CharField(max_length=250)
    knowledge = models.TextField()
    language_certificates = models.TextField()
    educationandexp = models.TextField()
    company_desc = models.TextField()



