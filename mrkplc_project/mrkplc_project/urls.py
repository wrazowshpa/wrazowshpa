"""mrkplc_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url,include
from mrkplc_forms_app import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('mrkplc_forms_app/', include(('mrkplc_forms_app.urls', 'mrkplc_forms_app'), namespace='mrkplc_forms_app')),
    path('mrkplc_users_app/', include(('mrkplc_users_app.urls', 'mrkplc_users_app'), namespace='mrkplc_users_app')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special,name='special'),
    path('mrkplc_search_app/', include(('mrkplc_search_app.urls', 'mrkplc_search_app'), namespace='mrkplc_search_app')),
]
