# -*- coding: utf-8 -*-

import json
import urllib
#import urllib2
import requests
import datetime
from dateutil.parser import *
TZOFFSETS = {"BRST": -10800}
from decimal import Decimal

from .models import Job, Description

def language_set(language):
    if "-" in language:
        return (language.split('-')[1]).upper()
    else:
        return language.upper()

def get_data():
    '''
    retrieves all the job posts available in both language
    from http://www.ottawacityjobs.ca/data/{en/fr}

    return:
        data= all job posts
    '''
    data = []
    for lang in ['en','fr']:
        response = requests.get('http://www.ottawacityjobs.ca/'+lang+'/data/'	)
        data.append(response.json())
    return data

def get_jobref_list(data):
    '''
    retrives a dict list of all the job references available
    on http://www.ottawacityjobs.ca/

    return:
       [{'jobref': '2015-EX-EN-51084750'}, ...]
    '''
    jobref = []
    for job in data[0]['jobs']:
        jobref.append({'jobref': job.get('JOBREF')})
    return jobref

def stringify_object(data):
    '''
    return a String version of a date
    '''
    expirydate = parse(data)
    expirydate = str(expirydate).split(' ')[0]
    return expirydate

def job_object_list():
    """
    This function will compare the list of Jobs
    from the DB with the list of jobs from the website 
    http://www.ottawacityjobs.ca/
    and if it s found new jobs it will save it to
    the DB
    """
    jobsDb = Job.objects.values('jobref')
    #flatten jobsDb
    jobs_db = [ i.get('jobref') for i in jobsDb]
    data = get_data()
    #print(data)
    list_emploi = []
    for job in [0,1]:
        for emploi in data[job]['jobs']:
            if emploi.get('JOBREF') not in jobs_db:
                #save Job to db
                #calcul
                salary = emploi.get('SALARYMAX', None)  
                if emploi.get('SALARYMAX', None):
                    if ',' in emploi.get('SALARYMAX', None):
                        salary = emploi.get('SALARYMAX', None)
                        salary = salary.replace(',', '')
                #create object
                emploi_model = Job( 
                    expirydate = stringify_object(emploi.get('EXPIRYDATE')),
                    job_summary = emploi.get('JOB_SUMMARY', None),
                    jobref = emploi.get('JOBREF', None),
                    language = (emploi.get('JOBREF', None)).split('-')[2],
                    joburl = emploi.get('JOBURL', None),
                    name = emploi.get('NAME', None),
                    position = emploi.get('POSITION', None),
                    pub_date =stringify_object(emploi.get('POSTDATE')),
                    salarymax =salary,
                    salarymin = emploi.get('SALARYMIN', None),
                )
                #save Description to db
                list_emploi.append( emploi.get('JOBREF'))
                #print(emploi_model.jobref)
                emploi_model.save()
                emploi_model.description_set.create(
                    knowledge = emploi.get('KNOWLEDGE', None),
                    languagecert = emploi.get('LANGUAGE_CERTIFICATES', None),
                    educationandexp = emploi.get('EDUCATIONANDEXP', None),
                    company_desc = emploi.get('COMPANY_DESC', None),
                    pub_date = stringify_object(emploi.get('POSTDATE'))
                        )
    #print(len(list_emploi))
                


class DecimalEncoder(json.JSONEncoder):
    """Utils so that the json file can 
    write the proper Datetime
    """
    def _iterencode(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)

def emplois():
    """
    This function does almost the same thing as 
    job_object_list()
    but it wont' save anything in the DB
    it will create a JSON file instead
    """
    data = get_data()
    conteneur = []
    compteur = 1
    for lang in [0,1]:
        for job in data[lang]['jobs']:
            expirydate = parse(job.get('EXPIRYDATE', None))
            expirydate = str(expirydate).split(' ')[0]
            pub_date = parse(job.get('POSTDATE', None))
            pub_date = str(pub_date).split(' ')[0]
            #calcul
            salary = job.get('SALARYMAX', None)
            if job.get('SALARYMAX', None):
                if ',' in job.get('SALARYMAX', None):
                    salary = job.get('SALARYMAX', None)
                    salary = (salary.replace(',', ''))
                    #salary = int(salary)
            conteneur.append(
            {
                "fields": {
                    "expirydate": expirydate,
                    "job_summary": job.get('JOB_SUMMARY', None),
                    "jobref": job.get('JOBREF', None),
                    "language": (job.get('JOBREF', None)).split('-')[2],
                    "joburl": job.get('JOBURL', None),
                    "name": job.get('NAME', None),
                    "position": job.get('POSITION', None),
                    "pub_date": pub_date,
                    "salarymax": salary,
                    "salarymin": job.get('SALARYMIN', None),
                    "salarytype": job.get('SALARYTYPE', None),
                },
                "model": "emplois.job",
                "pk": compteur
                },
                    )
            conteneur.append(
            {
                "fields": {
                    "jobs": compteur,
                    "knowledge": job.get('KNOWLEDGE', None),
                    "languagecert": job.get('LANGUAGE_CERTIFICATES', None),
                    "educationandexp": job.get('EDUCATIONANDEXP', None),
                    "company_desc": job.get('COMPANY_DESC', None),
                    "pub_date": pub_date
                },
                "model": "emplois.description",
                "pk": compteur
                },
                    )
            compteur = compteur + 1


    #print(conteneur)

    with open('uottawa_emplois_bilingual.json', 'w') as f:
      json.dump(conteneur, f, sort_keys = True, indent = 4, ensure_ascii=False, cls=DecimalEncoder)

    print('json file created: uottawa_emplois_bilingual.json')


#get each row into the db
''' shell
https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format

from applications.emplois.models import Description, Job
from applications.emplois.utils import emplois

emplois()

"JOBREF": "2016-EX-EN-51513638"

'''