from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    return render(request, 'listings/search.html')
