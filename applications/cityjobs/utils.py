# -*- coding: utf-8 -*-

import json
import os
from dateutil.parser import parse
from .models import Emploi, Description

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
        description = Description.objects.create(
        KNOWLEDGE = item.get('KNOWLEDGE'),
        LANGUAGE_CERTIFICATES = item.get('LANGUAGE_CERTIFICATES'),
        EDUCATIONANDEXP = item.get("EDUCATIONANDEXP"),
        COMPANY_DESC = item.get("COMPANY_DESC"),
        JOBURL = item.get("JOBURL"),
        JOB_SUMMARY = item.get("JOB_SUMMARY")
    )
        description.emploi_set.create(
        EXPIRYDATE = parse_date(item.get("EXPIRYDATE")),
        JOBREF = job_ref,
        LANGUAGE  = lang[2],
        JOBNAME = item.get('NAME'),
        POSITION = item.get('POSITION'),
        POSTDATE = parse_date(item.get('POSTDATE')),
        SALARYMIN = item.get('SALARYMIN'),
        SALARYMAX = item.get('SALARYMAX'),
        SALARYTYPE = item.get('SALARYTYPE')
     )
    return 'successful'


#load json files

#get each row into the db
''' shell
https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format

from applications.cityjobs.models import Description, Emploi
from applications.cityjobs.utils import open_json_file as main_app
from applications.cityjobs.utils import open_this_file as op 

Emploi.objects.all().delete()
Description.objects.all().delete()
data = op()
a = main_app(data)

"JOBREF": "2016-EX-EN-51513638"

'''