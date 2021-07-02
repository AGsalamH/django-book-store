from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product, Category

# Create your views here.


def all_products(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {
        'products': products
    })


def product_detail(request, slug):
    try:
        product = Product.products.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404('Product is NOT available.')
    return render(request, 'store/products/detail.html', {
        'product': product
    })


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.products.filter(category=category)

    return render(request, 'store/products/category.html', {
        'products': products,
        'category': category
    })
