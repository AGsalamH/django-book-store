from store.models import Product
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from .utils import Cart
from django.views.decorators.http import require_POST

# Create your views here.


def cart_summary(request):
    return render(request, 'carts/cart_summary.html', {
    })


@require_POST
def cart_add(request: HttpRequest):
    cart = Cart(request)

    product_id = request.POST.get('product_id')
    product_qty = request.POST.get('product_qty')
    product = Product.products.get(id=product_id)
    cart.add(product=product, qty=product_qty)
    return JsonResponse({
        'test': 'data'
    })
