import json

#pip fake-factory
from faker import Faker
fake = Faker()
import datetime
import random
import uuid


conteneur = []
today = datetime.date.today()
compteur = 1
for data in range(1,50):
	conteneur.append(
    {
        "fields": {
            "expirydate": str(today+datetime.timedelta(1*random.randint(1,30))),
            "job_summary": fake.paragraph(),
            "jobref": str(uuid.uuid4()),
            "joburl": fake.url(),
            "name": "City of Ottawa",
            "position": " ".join(fake.words(random.randint(4,9))),
            "pub_date": str(today-datetime.timedelta(1*random.randint(1,30))),
            "salarymax": str(random.randint(30000,76000)),
            "timestamps": str(today-datetime.timedelta(1*random.randint(1,30)))
        },
        "model": "emplois.job",
        "pk": compteur
    },
		)
	compteur = compteur + 1
#print(dir(fake))
#print(conteneur)




with open('emplois_fixtures.json', 'w') as f:
  json.dump(conteneur, f, sort_keys = True, indent = 4, ensure_ascii=False)

print('json file created: emplois_fixtures.json')