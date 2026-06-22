from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categort(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    Categort=models.ForeignKey(Categort,related_name='prodect',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='product',blank=True,null=True)
    Categort_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order{self.id}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.quantity}*{self.Product.name}"