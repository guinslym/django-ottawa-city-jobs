from rest_framework import serializers
from .models import Description, Emploi


class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description 
        fields = ('pk', 'JOBURL', 'KNOWLEDGE','LANGUAGE_CERTIFICATES',
            'EDUCATIONANDEXP','COMPANY_DESC','PUB_DATE','JOB_SUMMARY')



class EmploiSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()
    
    class Meta:
        model = Emploi 
        fields = (
            'pk', 'POSITION', 'JOBREF', 'LANGUAGE','JOBNAME',
            'POSTDATE','SALARYMIN','SALARYMAX','SALARYTYPE', 'description'
            )

