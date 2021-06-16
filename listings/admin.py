from django.contrib import admin

#Bring in the Listing Model from the models into this file
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'is_published', 'city', 'state', 'zipcode', 'realtor', 'price')
    list_display_links = ('title',)
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'state', 'realtor__name', 'zipcode')
    list_per_page = 25


#Register the Model 
admin.site.register(Listing, ListingAdmin)


