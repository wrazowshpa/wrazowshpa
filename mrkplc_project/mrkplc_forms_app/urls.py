from django.conf.urls import url
from . import views
from django.urls import path

#this is the app name that is referenced in the url before the individual paths
app_name = 'mrkplc_forms_app'

#url patterns for ad list, detail, update, delete, search, search detail, auth user
#ads, and auth user ad details
urlpatterns = [
    path('', views.AdListView.as_view(), name="list"),
    path('<int:pk>/', views.AdDetailView.as_view(), name='detail'),
    path('create/', views.PostAdCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PostAdUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostAdDeleteView.as_view(), name='delete'),
    path('search/', views.PostAdSearchResultsView.as_view(), name="search_results"),
    path('search/<int:pk>/', views.AdDetailView.as_view(), name='detail'),
    path('userads/', views.userprofile, name="user_ads"),
    path('userads/<int:pk>/',views.AdDetailView.as_view(), name='detail'),
]