from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProductForm
from .models import ProductModel

# Create your views here.


# 1. Signup View
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# 2. Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 3. Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# 4. Home Page
@login_required
def home_view(request):
    return render(request, 'home.html')

# 5. Product List (Card view)
def product_list(request):
    products = ProductModel.objects.all()
    return render(request, 'product_list.html', {'products': products})

# 6. Add Product
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form, 'title': 'Add Product'})

# 7. Edit Product
@login_required
def edit_product(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'title': 'Edit Product'})

# 8. View Product Details
def product_detail(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# 9. Delete Product
@login_required
def delete_product(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})