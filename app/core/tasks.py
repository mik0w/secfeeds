from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task
import feedparser
import requests
from core.models import FeedData, FeedMessage
import logging
from datetime import datetime
from dateutil.parser import parse



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
    NewsFeed = feedparser.parse(feed_url)
    entries = NewsFeed.entries
    print(str(entries))
    print(str(feed_url))
    for entry in entries:
        print(str(entry))
        title = str(entry['title'])
        summary = str(entry['summary'])
        published = parse(entry['published']) # parse method is from dateutil.parse 
        print(str(published) + '' + str(type(published)))
        link = str(entry['link'])
        feed_data = FeedData.objects.get(feed_url=feed_url)
        data = FeedMessage.objects.create(feed_kind=feed_data, title=title, summary=summary, published=published, link=link)
        data.save()
    pass





@task(name='refresh_feed')
def refresh_feed(feed_url : str):
    pass


# @shared_task
# def parse_feed(feed_url : str):
#     pass

