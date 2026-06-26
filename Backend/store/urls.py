from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('products/', views.get_products, name='get_product'),
    path('products/<str:pk>/', views.get_product, name='get_product'),
    path('categories/', views.get_categories, ),
    path('api/cart/', views.get_cart, name='get_cart'),
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
    path('api/cart/remove/', views.remove_from_cart, name='remove_from_cart'),
]
