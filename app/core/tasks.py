from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task
import feedparser
import requests
from core.models import FeedData
import logging


@task(name='check_feed')
def check_feed(feed_url : str):
    
    r = requests.get(feed_url)
    
    logging.basicConfig(format = '%(messages)s')
    log = logging.getLogger()
    log.warning("status code is: " + str(r.status_code))
    log.warning("feed url: " + feed_url)
    if r.status_code == 200:
        data = FeedData.objects.get(feed_url=feed_url)
        data.is_verified = True
        data.save()
        return True
    else: 
        return False

# @shared_task
# def parse_feed(feed_url : str):
#     pass

