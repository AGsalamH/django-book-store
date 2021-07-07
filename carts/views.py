# Django-specific
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST

# Custom
from .utils import Cart
from store.models import Product


def cart_summary(request):
    return render(request, 'carts/cart_summary.html')


@require_POST
def cart_add(request):
    cart = Cart(request)

    product_id = request.POST.get('product_id')
    product_qty = request.POST.get('product_qty')
    product: Product = get_object_or_404(Product, id=product_id)
    cart.add(product, qty=product_qty)
    return JsonResponse({'qty': cart.unique_items, 'subtotal': cart.get_total_price()})


@require_POST
def cart_delete(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    product_qty = request.POST.get('product_qty')
    product: Product = get_object_or_404(Product, id=product_id)

    cart.delete(product)
    return JsonResponse({'qty': cart.unique_items, 'subtotal': cart.get_total_price()})


@require_POST
def cart_update(request):
    cart = Cart(request)

    product_id = request.POST.get('product_id')
    product_qty = request.POST.get('product_qty')
    product: Product = get_object_or_404(Product, id=product_id)
    cart.update(product, qty=product_qty)
    return JsonResponse({'qty': cart.unique_items, 'subtotal': cart.get_total_price()})
