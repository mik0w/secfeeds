from django import forms
from core.models import FeedData


class CheckFeedForm(forms.Form):

    class Meta:
        model = FeedData
        fields = ['feed_url']

    feed_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Feed URL'}))

    def save(self): 
        data = self.cleaned_data
        feed_data = FeedData(feed_url=data['feed_url'])
        feed_data.save()



    