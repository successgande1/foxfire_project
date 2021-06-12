from django.contrib import admin

#Bring in the Listing Model from the models into this file
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'city', 'state', 'zipcode', 'realtor', 'price')
    list_display_links = ('title',)
    list_filter = ('city', 'state', 'realtor')
    search_fields = ('title', 'address', 'city', 'state', 'realtor')
    list_per_page = 25


#Register the Model 
admin.site.register(Listing, ListingAdmin)


