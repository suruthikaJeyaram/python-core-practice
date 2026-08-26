#shopping cart
class Product:
    def __init__(self,name,quantity,price):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_price(self):
        return self.price*self.quantity
    
class shoppingcart:
    def __init__(self):
        self.products=[]
    def add_product(self,name,quantity,price):
        for product in self.products:
            if product.name==name:
                 product.quantity+=quantity
                 print(f"{name} quantity updated")
                 return
        new_product=Product(name,quantity,price)
        self.products.append(new_product)
        print(f"{name} added to cart")
    def remove_product(self,name):
        for product in self.products:
            if product.name==name:
                self.products.remove(product)
                print(f"{name} removed from cart")
                return
        print("produt not found")
    def show_cart(self):
        print("\n shopping cart items")
        for product in self.products:
            print("name:",product.name)
            print("price:",product.price)
            print("quantity:",product.quantity)
            print("Total:",product.total_price())
            print("__________________")
    def cart_total(self):
        total=0
        for product in self.products:
            total+=product.total_price()
        return total
cart=shoppingcart()
cart.add_product ("rice",50,10)
cart.add_product("maida",40,5)
cart.add_product("jaggery",90,2)
cart.show_cart()
print("Total cart price=",cart.cart_total())
cart.remove_product("maida")
cart.show_cart()
print("Total cart price=",cart.cart_total())
            
