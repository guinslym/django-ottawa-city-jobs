from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Job(models.Model):

    def __str__(self):
        return self.position
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now
    def still_not_expired_job_list(self):
        now = timezone.now()
        return self.expirydate >= now 


    joburl = models.URLField(max_length=250)
    expirydate = models.DateField()
    salarymax = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=40) 
    position = models.CharField(max_length=150)
    jobref = models.CharField(max_length=30)
    job_summary = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

@python_2_unicode_compatible
class Description(models.Model):
    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    salarytype = models.CharField(max_length=250)
    knowledge = models.TextField()
    language_certificates = models.TextField()
    educationandexp = models.TextField()
    company_desc = models.TextField()



