from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserModel, ProductModel

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUserModel
        fields = ['username', 'full_name', 'email', 'date_of_birth', 'profile_image', 'user_types']

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['product_name', 'product_description', 'product_price', 'product_image']