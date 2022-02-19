from django.db import models
from datetime import date


class FeedData(models.Model):
    feed_url = models.URLField(max_length=350, unique=True)
    feed_name = models.CharField(max_length=250, default='')
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
          return self.feed_url

class FeedMessage(models.Model):
    feed_kind = models.ForeignKey(FeedData, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default = 'n/a')
    summary = models.TextField(default = 'n/a')
    published = models.DateField(default=date.today())
    link = models.URLField(max_length=350) #dodac unique=True

    def __str__(self):
        return self.title

