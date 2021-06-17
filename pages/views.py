from django.shortcuts import render

from listings.models import Listing

from realtors.models import Realtor

from django.http import HttpResponse

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings
    }
    return render(request, 'pages/index.html', context)

#About Page View
def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    #Get is_mvp Realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, 'pages/about.html', context)
