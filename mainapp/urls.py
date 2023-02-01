from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('faq.html', views.faq, name='faq'),
    path('about.html', views.about, name='about'),
]