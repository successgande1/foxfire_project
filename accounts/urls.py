from django.urls import path
#import the views module
from . import views

#Create url patterns
urlpatterns = [
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('logout', views.logout, name = 'logout')
]