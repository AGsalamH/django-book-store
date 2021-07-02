from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categories/<slug:slug>/', views.category_products, name='category')
]
