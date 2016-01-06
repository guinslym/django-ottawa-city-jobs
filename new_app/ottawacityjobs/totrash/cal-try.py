import time
import json
import datetime
import dateutil.parser
from random import choice

random_choice = lambda: choice([0,1,2,3,4,5])

with open('jobs_en.json') as data_file:   
  data = json.load(data_file)

json_data = {}
for job in data:
  #Parsing the string object
  la_date = dateutil.parser.parse(job['postdate'])
  #retrieving the date in second
  la_date = time.mktime(la_date.timetuple())
  chiffre = random_choice()
  if json_data.get(str(la_date), None) == None:
    json_data.update({la_date :chiffre})


with open('json_data_for_try.json', 'w') as outfile:
  json.dump(json_data, outfile, sort_keys = True, indent = 4,ensure_ascii=False)



print('done writing the json file')

'''
How to be proud
Calendar is working
Read book
Call Ditson
946721039
'''
