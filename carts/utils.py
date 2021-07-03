from django.http.request import HttpRequest
from store.models import Product
class Cart:
    def __init__(self, request:HttpRequest):
        self.session = request.session
        items = self.session.get('cart_items')
        if not 'cart_items' in self.session:
            items = self.session['cart_items'] = {}
        self.items = items
    
    @property
    def unique_items(self):
        return len(self.items.keys())

    def add(self, product:Product=None, qty:int=1):
       self.items.update({str(product.id): {
           'price': str(product.price),
           'name': product.name,
           'url': product.get_absolute_url(),
           'qty': qty,
        }})

       self.session.modified = True
    

    def remove(self, id):
        
        return
        

    def get_total_price(self):
        total = 0.00
        for item in self.items.values():
            total += float(item['price'])
        return total