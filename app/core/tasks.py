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
    feed_details = feedparser.parse(str(feed_url))
    try:
        title = feed_details.feed.title
    except AttributeError:
        title = False
    logging.basicConfig(format = '%(messages)s')
    log = logging.getLogger()
    log.warning("status code is: " + str(r.status_code))
    log.warning("feed url: " + feed_url)
    if r.status_code == 200 and title:
        data = FeedData.objects.get(feed_url=feed_url)
        data.is_verified = True
        data.feed_name=str(title)
        data.save()
        return True
    else: 
        return False

@task(name='download_feed')
def download_feed(feed_url : str):
    pass


@task(name='refresh_feed')
def refresh_feed(feed_url : str):
    pass


# @shared_task
# def parse_feed(feed_url : str):
#     pass

