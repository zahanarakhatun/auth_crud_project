from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'), # Root URL opens signup page as per note
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
]