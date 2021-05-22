from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.view_about, name='about'),
    path('contact/', views.view_contact, name='contact'),
    path('faqs/', views.view_faqs, name='faqs'),
]
