class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart=self.session["cart"] ={}
        self.cart = cart

    def add(self,producto):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id_producto]={
                "producto_id":producto.id_producto,
                "producto":producto.producto,
                "cantidad":1,
                "precio":producto.precio,
                "imagen":producto.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id_producto):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self,producto):
        produc_id = str(producto.producto_id)
        if produc_id in self.cart:
            del self.cart[produc_id]
            self.save()

    def decrement(self,producto):
        for key, value in self.cart.items():
            if key == str(producto.id_producto):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"] < 1:
                    self.remove(producto)
                self.save()
                break
            else:
                print("el producto no existe")
    
    def clear(self):
        self.session["cart"] ={}
        self.session.modified = True

