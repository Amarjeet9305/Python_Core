# By using polymorphism calculate the product price with or without discount 

class Order:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
# Calculate total price "Polymorphism method calling"     
    def calculate_price(self):
        return self.price * self.quantity
# Product discount in child class 'Polymorphism'
class DiscountedProduct(Order):
    def __init__(self, name, price, quantity, discount_percent):
        super().__init__(name, price, quantity)
        self.discount_percent = discount_percent 
         
# Calculate total price with discount and without discount        
    def calculate_price(self):
        
        total = super().calculate_price()
        discount = (self.discount_percent / 100) * total
        return total - discount       

# Function to display final price (polymorphic behavior)

def show_final_price(product_obj):
    print(f"Product: {product_obj.name}")
    print(f"Final Price: ₹{product_obj.calculate_price()}")    
    
# Object without discount
p1 = Order("Laptop Bag", 1500, 2)

# Object with discount
p2 = DiscountedProduct("Laptop Bag", 1500, 2, 10)

# Polymorphism in instance calling

# Without discount "obj1"
show_final_price(p1) 
 
# With discount "obj2" 
        
show_final_price(p2)     
        
           

        