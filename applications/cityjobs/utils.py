# -*- coding: utf-8 -*-

import json
import os
from dateutil.parser import parse
from .models import Job, Description

def parse_date(this_date):
    this_date = parse(this_date)
    this_date = this_date.strftime('%Y-%m-%d')
    return this_date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def open_this_file():
    with open('a.json') as data_file:
        data = json.load(data_file)
    data = data['jobs']
    return data

#get the absolute path
def open_json_file(data):
    for item in data:
        job_ref = item.get("JOBREF")
        lang = job_ref.split('-')
        job = Job.objects.create(
        company_desc = item.get("COMPANY_DESC"),
        educationandexp = item.get("EDUCATIONANDEXP"),
        expirydate = parse_date(item.get("EXPIRYDATE")),
        joburl = item.get("JOBURL"),
        jobref = job_ref,
        job_summary = item.get("JOB_SUMMARY"),
        knowledge = item.get('KNOWLEDGE'),
        language_certificates = item.get('LANGUAGE_CERTIFICATES'),
        language  = lang[2],
        jobname = item.get('NAME'),
        position = item.get('POSITION'),
        postdate = parse_date(item.get('POSTDATE')),
        salarymin = item.get('SALARYMIN'),
        salarymax = item.get('SALARYMAX'),
        salarytype = item.get('SALARYTYPE')
    )
        job.description_set.create(
        knowledge = item.get('KNOWLEDGE'),
        language_certificates = item.get('LANGUAGE_CERTIFICATES'),
        educationandexp = item.get("EDUCATIONANDEXP"),
        company_desc = item.get("COMPANY_DESC")
     )
    return 'successful'



#load json files

#get each row into the db
''' shell
https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format

from applications.cityjobs.models import Description, Job
from applications.cityjobs.utils import open_json_file as main_app
from applications.cityjobs.utils import open_this_file as op 

Job.objects.all().delete()
Description.objects.all().delete()
data = op()
a = main_app(data)

"JOBREF": "2016-EX-EN-51513638"

'''