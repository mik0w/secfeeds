from django.shortcuts import render
from core.models import FeedData
from core.forms import CheckFeedForm
from core.tasks import check_feed


def feed_details(request, feed_id):
    feed = FeedData.objects.get(pk=feed_id)
    return render(request, 'feed_reader/feed_details.html', {'feed': feed})

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


    def verify_feed(self):
        if check_feed():
            pass
        else:
            return False



