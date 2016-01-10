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

class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)

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

def hello():
    import random, datetime
    number = str(random.randint(2,2000))+'.json'
    conteneur = {'hello', datetime.datetime.time().now()}
    with open(number, 'w') as f:
        json.dump(conteneur, f, sort_keys = True, indent = 4, ensure_ascii=False, cls=DecimalEncoder)

print('json file created: uottawa_emplois_bilingual.json')

