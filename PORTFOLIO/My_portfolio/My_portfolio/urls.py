# urls.py
from django.urls import path
from .views import index, home, about, contact, projects

urlpatterns = [
    #path('', home, name='home'),
    #path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('home/',index,name='home'),
    path('contact/',contact,name='contact'),
    path('',about,name='about'),
    # Add more URL patterns for additional pages
]
