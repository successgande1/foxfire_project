from django.urls import path
#import the views module
from . import views

#Create url patterns
urlpatterns = [
    path('', views.index, name = 'listings'),
    path('<int:listing_id>', views.listing, name = 'listing'),
     path('search', views.search, name = 'search'),
]