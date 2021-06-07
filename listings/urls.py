from django.urls import path
#import the views module
from . import views

#Create url patterns
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
]