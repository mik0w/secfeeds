from django.db import models


class FeedData(models.Model):
    feed_url = models.CharField(max_length=350, primary_key=True)
    feed_name = models.CharField(max_length=250, default='')
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.feed_url

