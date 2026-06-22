from django.contrib import admin
from .models import Categort,Product,UserProfile,Order,OrderItem

# Register your models here.
admin.site.register(Categort)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
