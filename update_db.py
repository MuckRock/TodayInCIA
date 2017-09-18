import requests
from db import RPiBlogDatabase

import unicodecsv
import json

csvFiles = True
csvNumber = 1

while CSVfiles:
    open('crest_lite_' + csvNumber + '.csv') as csvfile



db = RPiBlogDatabase()

url = 'https://www.raspberrypi.org/wp-json/wp/v2/posts?per_page=100'

posts = True
csvNumber = 1

while posts:

    for post in posts:
        slug = post['slug']
        title = post['title']['rendered']
        pub_date = post['date']
        if db.get_post_by_slug(slug):
            posts = False
        else:
            print('Adding {}'.format(slug))
            db.insert_post(slug, title, pub_date)
    page += 1
