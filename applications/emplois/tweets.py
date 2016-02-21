# -*- coding: utf-8 -*-

import tweepy
import time, sys, os
from .models import Job


#@cityofottawajob 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY=os.environ.get("CONSUMER_KEY")#keep the quotes, replace this with your consumer key
CONSUMER_SECRET=os.environ.get("CONSUMER_SECRET")#keep the quotes, replace this with your consumer secret key
ACCESS_KEY=os.environ.get("ACCESS_KEY")#keep the quotes, replace this with your access token
ACCESS_SECRET=os.environ.get("ACCESS_SECRET")#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#for line in f:
    #api.update_status(line)
    #time.sleep(900)#Tweet every 15 minutes

def tweet_a_job():
    '''Fetch a job in english and in french'''
    emplois = []
    job = Job.objects.filter(tweeted=False).order_by('?').first()
    if not job:
        #There is nothing to Tweet
        return 0
    job_number = job.jobref.split('-')[3]
    jobs = Job.objects.filter(jobref__contains=job_number)
    for job in jobs:
        publish_tweet(job,job.language)
        #job.tweeted = True
        #job.save()



def publish_tweet(job, language):
    """Publishing a tweet in each language"""
    from random import randint
    print("\nIn publish tweet ")
    line = "\nNo VALUE\n"
    #Construct the twwet in English or in French
    if language == 'FR':
        job_position = ( "Offre d'emploi #" + str(randint(0,100)) + " - ville D'#Ottawa: " +job.position) if (len( "Offre d'empoi #" + str(randint(0,100)) + " de la ville D'#Ottawa: " +job.position) < 117) else job.position[0:115]
        line = job_position + " " + job.joburl
        #print("IN FR")
    if language == 'EN':
        job_position =  ("Job #" + str(randint(0,100)) + " from the city of #Ottawa: " +job.position) if (len( "#Ottawa city jobs #" + str(randint(0,100)) + ": " +job.position) < 117) else job.position[0:115]
        line = job_position + " " + job.joburl
        #print("IN EN")
    try:
        #Tweet it on Twitter
        print(line)
        #api.update_status(status=line)
    except tweepy.error.TweepError:
        pass
    time.sleep(5)
    pass