import json
import urllib
#import urllib2
import requests
import datetime
from dateutil.parser import *
TZOFFSETS = {"BRST": -10800}
from decimal import Decimal

def get_data():
    data = []
    for lang in ['en','fr']:
        response = requests.get('http://www.ottawacityjobs.ca/'+lang+'/data/'	)
        data.append(response.json())
    return data

'''
resource_url = 'http://localhost:8080/service/'
resource_url = 'http://www.ottawacityjobs.ca/en/data/'
response = json.loads(urllib2.urlopen(resource_url).read())
print(response)
'''

'''
r = urllib.request.urlopen(url)
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
print(data)
'''

'''
def get_jobs(data):
    job_list = []
    for job in data['jobs']:
        new_job = {'position' : job.get('POSITION', None),
            'joburl' : job.get('JOBURL', None),
            'postdate' : job.get('POSTDATE', None),
            'expirydate' :job.get('EXPIRYDATE', None),
            'salarymax': job.get('SALARYMAX', None),
            'name': job.get('NAME', None),
            'jobref': job.get('JOBREF', None),
            'job_summary': job.get('JOB_SUMMARY', None),
            #EXTRA
            'salarytype': job.get('SALARYTYPE', None),
            'knowledge':job.get('KNOWLEDGE', None),
            'language_certificates' : job.get('LANGUAGE_CERTIFICATES', None),
            'educationandexp': job.get('EDUCATIONANDEXP', None)
            'company_desc': job.get('COMPANY_DESC', None)
            }
        job_list.append(new_job)
        print("\n")
        print(new_job)
    return job_list
'''

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
        if job.get('SALARYMAX', None):
            if ',' in job.get('SALARYMAX', None):
                salary = job.get('SALARYMAX', None)
                salary = (salary.replace(',', ' '))
                #salary = int(salary)
        else:
            salary = None
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
                "salarymax": salary
            },
            "model": "emplois.job",
            "pk": compteur
            },
                )
        conteneur.append(
        {
            "fields": {
                "jobs": compteur,
                "salarytype": job.get('SALARYTYPE', None),
                "knowledge": job.get('KNOWLEDGE', None),
                "languagecert": job.get('LANGUAGE_CERTIFICATES', None),
                "educationandexp": job.get('EDUCATIONANDEXP', None),
                "company_desc": job.get('COMPANY_DESC', None),
                "salarymin": job.get('SALARYMIN', None),
                "pub_date": pub_date
            },
            "model": "emplois.description",
            "pk": compteur
            },
                )
        compteur = compteur + 1


#print(conteneur)

with open('uottawa_emplois_bilingual.json', 'w') as f:
  json.dump(conteneur, f, sort_keys = True, indent = 4, ensure_ascii=False)

print('json file created: uottawa_emplois_bilingual.json')


"""
#To write to file as a backup
with open('jobs_fr.json', 'w') as outfile:
	json.dump(job_list, outfile, sort_keys = True, indent = 4,ensure_ascii=True)
"""

"""	
https://wa0x6e.github.io/cal-heatmap/v2/

#unixtimestamp and number of Work published for that day
{
  "946705035": 4,
  "946706692": 4,
  "946707210": 0
}
https://wa0x6e.github.io/cal-heatmap/v2/datas-years.json

command line
date -d @946707210 +'%Y-%m-%d %H:%M:%S'
There is NO space after the + sign
"""


"""
Calculate the number of days between to date

from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d0 - d1
print delta.days
"""


"""
Database for Django
--Jobs
--Language
--Profile (details)
"""

