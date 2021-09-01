class Cart:
    def __init__(self, request):
        if request.session.get('cart') is None:
            request.session['cart'] = {}

        self.cart = request.session["cart"]
        self.session = request.session
    
    def add(self, product):
        self.cart[str(product.id)] = {
            "quantity":1, 
            "price": str(product.price),
        }

        self.session.modified = True
    