# -*- coding: utf-8 -*-

from .models import Job
import json

#get the absolute path
def open_json_file():
    with open('data.json') as data_file: 
        data = json.load(data_file)
    return data


#load json files

#get each row into the db
for item in data:
    cdesc = item.get('')
    eduexp = item.get('')
    expdate =
    jref = 
    jurl = 
    jsumm = 
    know =
    lang_cert = 
    n = 
    posit = 
    pdate =
    smax = 
    smin = 
    stype =
    Job.objects.create(
       dd
       dd
       dd
       dd
            )



