from django.shortcuts import render

# Create your views here.

def search(request):

    query = request.GET.get('q')
    results = PostAd.objects.annotate(search=SearchVector('body_text'),).filter(search=query)

    return render(request, 'mrkplc_search_app/results.html',{'results': results})