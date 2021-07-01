from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product, Category

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {
        'products': products
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {
        'product': product
    })


def category(request, slug):
    c = get_object_or_404(Category, slug=slug)
    products = c.products.all()

    return render(request, 'store/products/category.html', {
        'products': products,
        'category': c
    })