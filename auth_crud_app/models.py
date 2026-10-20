
from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE_CHOICES = (
    ('Customer', 'Customer'),
    ('Owner', 'Owner'),
)

class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    user_types = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Customer')

    def __str__(self):
        return self.username

class ProductModel(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name