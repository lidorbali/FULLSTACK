from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('products/<id>', views.products),
]
