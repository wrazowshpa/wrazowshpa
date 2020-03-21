from django.db import models
from mrkplc_forms_app.choices import *
from django.urls import reverse
# from django.contrib.gis.geoip2 import GeoIP2
from django.urls import reverse
from mrkplc_users_app.models import UserProfileInfo
from django.utils import timezone


#this is the model for the ads
class PostAd(models.Model):
    # id = models.IntegerField(primary_key = True, unique= True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', db_column='username', on_delete=models.CASCADE)
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=50)
    ad_type = models.CharField(choices = AD_TYPE_CHOICES, max_length=50)
    for_sale_by = models.CharField(choices = FOR_SALE_BY_CHOICES, max_length=50)
    ad_title = models.CharField(max_length=100)
    # description = models.CharField(max_length=256)
    description = models.TextField(max_length=3000)
    images = models.ImageField(upload_to="media/", blank=True)
    youtube_video_link = models.URLField()
    website_url_link = models.URLField()
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    price_options = models.CharField(choices = PRICE_CHOICES, max_length=50)
    phone_num = models.CharField(max_length=50)
    email = models.EmailField(help_text="A valid email address, please")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.ad_title

    def get_absolute_url(self):
        return reverse("mrkplc_forms_app:detail", kwargs={'pk':self.pk})
