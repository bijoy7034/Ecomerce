from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

