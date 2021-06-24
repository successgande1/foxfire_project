from django.shortcuts import render

from listings.models import Listing

from realtors.models import Realtor

from django.http import HttpResponse

from listings.choices import bedrooms_choices, city_choices, state_choices, price_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'state_choices' : state_choices,
        'bedrooms_choices' : bedrooms_choices,
        'city_choices' : city_choices,
        'price_choices' : price_choices
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
