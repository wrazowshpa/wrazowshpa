from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'mrkplc_users_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),

]
