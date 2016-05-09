# -*- coding: utf-8 -*-

import json
import os
from .models import Job

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#get the absolute path
def open_json_file():
    with open('/a.json') as data_file: 
        data = json.load(data_file)
    for item in data['jobs']:
        Job.objects.create(
        company_desc = item.get("COMPANY_DESC"),
        educationandexp = item.get("EDUCATIONANDEXP"),
        expirydate = item.get("EXPIRYDATE"),
        joburl = item.get("JOBURL"),
        jobref = item.get("JOBREF"),
        job_summary = item.get("JOB_SUMMARY"),
        knowledge = item.get('KNOWLEDGE'),
        language_certificates = item.get('LANGUAGE_CERTIFICATES'),
        language  = item.get('LANGUAGE'),
        name = item.get('NAME'),
        position = item.get('POSITION'),
        postdate = item.get('POSTDATE'),
        salarymin = item.get('SALARYMIN'),
        salarymax = item.get('SALARYMAX'),
        salarytype = item.get('SALARYTYPE')
    )
    return data



#load json files

#get each row into the db
''' shell
https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format

import json
import os
from applications.cityjobs.models import Job 
from applications.cityjobs.utils import open_json_file
from ottawacityjobs.settings import BASE_DIR

with open(BASE_DIR+'/a.json') as data_file: 
    data = json.load(data_file)

for item in data['jobs']:
    Job.objects.create(
    company_desc = item.get("COMPANY_DESC"),
    educationandexp = item.get("EDUCATIONANDEXP"),
    expirydate = item.get("EXPIRYDATE"),
    joburl = item.get("JOBURL"),
    jobref = item.get("JOBREF"),
    job_summary = item.get("JOB_SUMMARY"),
    knowledge = item.get('KNOWLEDGE'),
    language_certificates = item.get('LANGUAGE_CERTIFICATES'),
    language  = item.get('LANGUAGE', 'EN'),
    name = item.get('NAME'),
    position = item.get('POSITION'),
    postdate = item.get('POSTDATE'),
    salarymin = item.get('SALARYMIN'),
    salarymax = item.get('SALARYMAX'),
    salarytype = item.get('SALARYTYPE')
)
'''