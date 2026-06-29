from django.contrib import admin
# Fixed spelling from Categort to Category
from .models import Category, Product, UserProfile, Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)