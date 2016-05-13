from rest_framework import serializers
from .models import *

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job 
        fields = ('pk', 'position', 'jobname','jobref', 'joburl','expirydate','salarytype')

'''
    expirydate = models.DateTimeField(auto_now=False, blank=True, null=True)
    joburl = models.URLField(max_length=250, blank=True, null=True)
    jobref = models.CharField(max_length=30, unique=True, blank=True, null=True)
    job_summary = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, default=ENGLISH) 
    jobname = models.URLField(max_length=250, blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    postdate = models.DateTimeField(auto_now=False, blank=True, null=True)
    salarymin = models.CharField(max_length=40, blank=True, null=True)
    salarymax = models.CharField(max_length=40, blank=True, null=True)
    salarytype = models.CharField(max_length=20, blank=True, null=True)
    tweeted = models.BooleanField(default=False)
    slug = models.CharField(max_length=200, blank=True, null=True)
'''

class DescriptionSerializer(serializers.ModelSerializer):
    #description = JobSerializer()
    #shelves = ShelfSerializer(many=True)
    #books = BookSerializer(many=True)

    class Meta:
        model = Description 
        fields = ('pk', 'jobs', 'knowledge')
        