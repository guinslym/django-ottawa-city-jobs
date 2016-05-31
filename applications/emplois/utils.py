# -*- coding: utf-8 -*-

import json
import urllib
from .models import Job, Description
from dateutil.parser import *

def stringify_object(data):
    '''
    return a String version of a date
    '''
    expirydate = parse(data)
    expirydate = str(expirydate).split(' ')[0]
    return expirydate

#is there a 'full.json' file?
def is_there_a_new_json_file():
    import os.path
    if os.path.isfile('full.json'):
        return True
    else:
        return False

#load it
def get_the_data_from_this_file():
    with open('full.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data

def insert_this_job_in_the_db(job):
    salary = job.get('SALARYMAX', None)
    if salary:
        if ',' in salary:
            salary = salary.replace(',', '')
    emploi_model = Job(
        JOBURL = job.get('JOBURL', None),
        EXPIRYDATE =  stringify_object(job.get('EXPIRYDATE', None)),
        SALARYMAX =  job.get('SALARYMAX', None),
        SALARYMIN =  job.get('SALARYMIN', None),
        SALARYTYPE = job.get('SALARYTYPE', None),
        NAME =  job.get('NAME', None),
        language = job.get('JOBREF', None).split('-')[2],
        POSITION =  job.get('POSITION', None),
        JOBREF = job.get('JOBREF', None),
        JOB_SUMMARY =job.get('JOB_SUMMARY', None),
    )
    #save Description to db
    #list_emploi.append( emploi.get('JOBREF'))
    #print(emploi_model.jobref)
    emploi_model.save()
    emploi_model.description_set.create(
        KNOWLEDGE = job.get('KNOWLEDGE', None),
        LANGUAGE_CERTIFICATES = job.get('LANGUAGE_CERTIFICATES', None),
        EDUCATIONANDEXP = job.get('EDUCATIONANDEXP', None),
        COMPANY_DESC = job.get('COMPANY_DESC', None),
            )

def check_in_the_db(data):
    for job in data:
        jobref = job.get('JOBREF')
        result = Job.objects.filter(JOBREF=jobref)
        if result:
            print('Already in the DB')
        else:
            insert_this_job_in_the_db(job)

def process_it():
    file_exist = is_there_a_new_json_file()
    if file_exist:
        data = get_the_data_from_this_file()
        check_in_the_db(data)
        return True
    return False

if __name__ == "__main__":
    #is_there_a_new_json_file()
    #get_the_data_from_this_file()
    pass
