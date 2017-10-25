import tweepy
import datetime
from time import sleep
from credentials import *
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# my_file=open('verne.txt','r')
# file_lines=my_file.readlines()
# my_file.close()

# See http://strftime.org

#datetime.datetime.now()
todays_date = datetime.date.today().strftime("%m") + "-" + datetime.date.today().strftime("%d")
print "it's " + todays_date
todays_file = open(todays_date + '.csv', 'r')
todays_list = []
for entry in todays_file.readlines():
    todays_list.append(entry.rstrip('\n'))



#my_file=open('verne.txt','r')

while True:
    print "check if it's still " + todays_date
    if todays_date == datetime.date.today().strftime("%m") + "-" + datetime.date.today().strftime("%d"):
        print "Same day, new demons"
        try:
            current_tweet = random.randint(0,len(todays_list))
            print(todays_list[current_tweet])
            api.update_status(todays_list[current_tweet])
            del todays_list[current_tweet]
        except tweepy.TweepError as e:
            print(e.reason)

    else:
        try:
            todays_date = datetime.date.today().strftime("%m") + "-" + datetime.date.today().strftime("%d")
            print "it's a new day! it's " + todays_date
            todays_file = open(todays_date + '.csv', 'r')
            todays_list = []
            tweet_counter = 0
            for entry in todays_file.readlines():
                todays_list.append(line.rstrip('\n'))
        except:
            print "Error on grabbing a new date file"
    sleep(1800)
