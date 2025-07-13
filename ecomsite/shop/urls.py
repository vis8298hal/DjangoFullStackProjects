from django.contrib import admin
from django.urls import path
from .views import show_products

urlpatterns = [
    path('', show_products, name='index'),
]