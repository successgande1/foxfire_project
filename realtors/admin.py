from django.contrib import admin

# Import the Realtor Model 
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'hire_date')
    search_fields = ('name',)
    #list_editable = ('is_mvp',)
    list_per_page = 25
    

#Register the Realtor App Model
admin.site.register(Realtor, RealtorAdmin)