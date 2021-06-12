from django.contrib import admin

# Import the Realtor Model 
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'hire_date')
    search_fields = ('name',)
    list_per_per = 25
    

#Register the Realtor App Model
admin.site.register(Realtor, RealtorAdmin)