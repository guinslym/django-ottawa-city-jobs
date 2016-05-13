from django.shortcuts import render

# Create your views here.
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import Job, Description

@api_view(['GET'])
def all_jobs(request, **kwargs):
    jobs = Job.objects.all()[0:4]
    
    serializers = JobSerializer(jobs, many=True)
    return Response(serializers.data)