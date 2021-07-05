from django.http.request import HttpRequest
from store.models import Product


class Cart:
    def __init__(self, request:HttpRequest):
        self.session = request.session
        self.items = self.session.get('cart_items')
        if not self.items:
            self.items = self.session['cart_items'] = {}

    def save(self):
        '''Saving the session'''
        self.session.modified = True

    def add(self, product:Product, qty:int=1):
        '''
        Adding and updating the users session cart_items 
        '''
        product_id = str(product.id) 
        if product_id in self.items:
            self.session[product_id]['qty'] = qty
        else:
            self.session[product_id] = {
                'name': product.name,
                'price': str(product.price),
                'url': product.get_absolute_url(), 
                'qty': qty,
            }
        self.save()
    
    def update(self, product:Product, qty:int=1):
        """
        Update values in session data
        """
        product_id = str(product.id) 
        if product_id in self.items:
            self.session[product_id]['qty'] = qty
            self.save()
        else:
            self.add(product, qty=qty)

    def delete(self, product:Product):
        """
        Delete item from session data
        """
        product_id = str(product.id)
        if product_id in self.items:
            del self.session[product_id]
            self.save()

    def get_total_price(self):
        total = 0.00
        for item in self.items.values():
            total += float(item['price'])
        return total


'''
    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

'''