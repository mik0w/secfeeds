from django.shortcuts import render
from core.models import FeedData, FeedMessage
from core.forms import CheckFeedForm
from core.tasks import check_feed, download_feed


def feed_details(request, feed_id):
    feed = FeedData.objects.get(pk=feed_id)
    feed_messages = FeedMessage.objects.filter(feed_kind=feed)
    print(feed_messages)
    return render(request, 'feed_reader/feed_details.html', {'feed': feed, 'feed_messages': feed_messages})

def feed_download(request, feed_id):
    feeds = FeedData.objects.all()
    feed = FeedData.objects.get(pk = feed_id)
    feed_url = feed.feed_url
    download_feed.apply_async(args=[feed_url], countdown=5)
    return render(
                    request, 
                    'feed_reader/feed_import.html',
                    {
                    'message': {'title': 'Feed data is being downloaded!'},
                    'feeds': feeds
                })

def feed_import(request):
    feeds = FeedData.objects.all()
    form = CheckFeedForm()
    if request.method == "POST":
        form = CheckFeedForm(request.POST)
        if form.is_valid():
            form.save()
            feed_url = form.cleaned_data.get("feed_url")
            check_feed.apply_async(args=[feed_url], countdown=5)
            return render(
                    request, 
                    'feed_reader/feed_import.html',
                    {
                    'message': {'title': 'Feed is being verified!'},
                    'feeds': feeds
                })
    
        else:
            form = CheckFeedForm()
    return render(request, 'feed_reader/feed_import.html', {'form': form, 'feeds': feeds})


def feed_refresh(request, feed_id):
    
    feed_data = FeedData.objects.get(pk=feed_id)
    feeds = FeedData.objects.all()
    
    return render(
                    request, 
                    'feed_reader/feed_import.html',
                    {
                    'message': {'title': 'Feed ' + str(feed_id) + ' (' + str(feed_data) + ')' + ' is being refreshed!'},
                    'feeds': feeds
                })


def verify_feed(self):
    if check_feed():
        pass
    else:
        return False



