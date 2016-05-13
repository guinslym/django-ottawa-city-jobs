from django.shortcuts import render

# Create your views here.
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import Emploi, Description

@api_view(['GET'])
def all_jobs(request, **kwargs):
    emplois = Emploi.objects.all()
    
    serializers = EmploiSerializer(emplois, many=True)
    return Response(serializers.data)
'''
@api_view(['GET'])
def all_descriptions(request, **kwargs):
    descriptions = Description.objects.all()[0:2]
    
    serializers = DescriptionSerializer(descriptions, many=True)
    return Response(serializers.data)
@api_view(['GET'])
def get_user(request, **kwargs):
    jobref = request.data['jobref']
    
    job = Job.objects.get(jobref=jobref)
    serializer = GRUserSerializer(job)
    return Response(serializer.data)
'''