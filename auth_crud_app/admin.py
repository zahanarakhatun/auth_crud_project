from django.contrib import admin
from .models import CustomUserModel, ProductModel

# Custom User মডেল রেজিস্টার করার জন্য
@admin.register(CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'user_types', 'is_staff')

# Product মডেল রেজিস্টার করার জন্য
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'created_at')