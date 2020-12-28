from django.shortcuts import render
from core.models import FeedData
from core.forms import CheckFeedForm
from core.tasks import check_feed


def feed_list(request):
    feeds = FeedData.objects.all()
    return render(request, 'feed_reader/feed_list.html', {'feeds': feeds})

def feed_import(request):
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
                    'message': {'title': 'Feed is being verified!'}
                })
    
        else:
            form = CheckFeedForm()
    return render(request, 'feed_reader/feed_import.html', {'form': form})


    def verify_feed(self):
        if check_feed():
            pass
        else:
            return False



