from django.contrib import admin
from core.models import FeedData
from core.models import FeedMessage

# Register your models here.


admin.site.register(FeedData)
admin.site.register(FeedMessage)
# register verified_feeds