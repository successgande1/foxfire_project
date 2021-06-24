from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.choices import bedrooms_choices, city_choices, state_choices, price_choices

#Import the Listing Model
from . models import Listing

# Create your views here.
def index(request):
    #Create variable and call the Listing Class Method with the Objects method with filter
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    content = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html', content)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    context = {
        'listing' : listing 
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #Check for Keywords search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        #This ensures that we don't get an empty string on our queryset
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    #Check for City search
    if 'city' in request.GET:
        city = request.GET['city']
        #This ensures that we don't get an empty string on our queryset
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #Check for City search
    if 'state' in request.GET:
        state = request.GET['state']
        #This ensures that we don't get an empty string on our queryset
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #Check for Bedrooms search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        #This ensures that we don't get an empty string on our queryset
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #Check for Price search
    if 'price' in request.GET:
        price = request.GET['price']
        #This ensures that we don't get an empty string on our queryset
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    context = {
        'listings':queryset_list,
        'state_choices' : state_choices,
        'bedrooms_choices' : bedrooms_choices,
        'city_choices' : city_choices,
        'price_choices' : price_choices,
        'values' : request.GET
    }
    return render(request, 'listings/search.html', context)
