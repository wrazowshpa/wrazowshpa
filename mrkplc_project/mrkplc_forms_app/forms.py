from django.forms import ModelForm
from ..mrkplc_forms_app.models import PostAd, SearchQuery
from django import forms

#this is the postadform, it is a modelform based on the model, all fields
#are presented when creating an ad

class PostAdForm(ModelForm):
    class Meta():
        model = PostAd
        fields = '__all__'


#class SearchQueryForm(ModelForm):
 #   class Meta():
  #      model = SearchQuery
   #     fields = '__all__'
