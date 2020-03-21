from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.contrib.postgres.search import SearchVector
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from mrkplc_forms_app.models import PostAd
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

#this is the index page/ landing page
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

#login url is in settings.py , this check if you are logged in, if not then you
#are shown that you need to login ... either login or logout is shown
@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    #return HttpResponseRedirect(reverse('index'))
    return render(request, 'index.html', {})

class AdListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    context_object_name = 'ads'
    model = models.PostAd

class AdDetailView(DetailView):
    template_name = 'mrkplc_forms_app/ad_detail.html'
    context_object_name = 'ad_details'
    model = models.PostAd

class PostAdCreateView(LoginRequiredMixin, CreateView):
    # template_name = 'mrkplc_forms_app/postad_form.html'
    model = models.PostAd
    fields = ['category', 'ad_type', 'for_sale_by', 'ad_title', 'description', 'images',
              'youtube_video_link', 'website_url_link', 'city', 'price','price_options', 'phone_num',
              'email',]

    # fields = '__all__'

    #before the form is submitted the authenticated user is assigned as the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostAdCreateView, self).form_valid(form)

class PostAdUpdateView(UpdateView):
    model = models.PostAd
    # fields = ['ad_type', 'for_sale_by', 'ad_title', 'description', 'images',
    #          'youtube_video_link', 'website_url_link', 'city', 'price', 'phone_num',
    #          'email',]
    fields = '__all__'

    success_url = reverse_lazy('mrkplc_forms_app:list')

class PostAdDeleteView(DeleteView):
    model = models.PostAd
    success_url = reverse_lazy('mrkplc_forms_app:list')


#this is the ordinary search that a user will do on the ad list page
class PostAdSearchResultsView(ListView):
    """
    Display a Blog List page filtered by the search query.
    """
    model = models.PostAd
    template_name = 'mrkplc_forms_app/results.html'
    context_object_name = 'ads'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PostAd.objects.annotate(search=SearchVector('ad_title', 'description'),).filter(search = query)
        #object_list = PostAd.objects.filter(Q(ad_title__icontains=query) | Q(description__icontains=query))
        return object_list

#class UserPostAdListView(ListView):
 #   model = models.PostAd
  #  template_name = 'mrkplc_forms_app/userads.html'
   # context_object_name = 'ads'
    #paginate_by = 10
#
 #   def get_queryset(self):
  #      return PostAd.objects.filter(owner=self.request.user)

#this is the user profile page that is loaded when the user
#clicks on my ads
@login_required #(login_url='/accounts/login/')
def userprofile(request):
    user = request.user
    user_posts = PostAd.objects.filter(author=request.user).order_by('-published_date')
    template = 'mrkplc_forms_app/userads.html'

    return render(request, template, {'user_posts': user_posts, 'user': user})

#add a redirect url if user is not logged in
