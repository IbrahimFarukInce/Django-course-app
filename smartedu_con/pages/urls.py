from django.contrib import admin
from django.urls import path, include
from pages.views import Aboutview, Indexview, ContactView

urlpatterns = [
    path('', Indexview.as_view(), name='index',),
    path('about/', Aboutview.as_view(), name='about',),
    path('contact/', ContactView.as_view(), name='contact',),


    
]