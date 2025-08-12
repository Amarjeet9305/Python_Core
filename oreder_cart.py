class order:
    def __init__(self,product,price,quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
# Creating a Child class    
class discount_order(order):
    def __init__(self, product, price, quantity, discount_percent):
        # Call parent class constructor
        super().__init__(product, price, quantity)
        self.discount_percent = discount_percent

    def final_price(self):
        total = self.total_price()
        discount_amount = (self.discount_percent / 100) * total
        return total - discount_amount

    def display_order(self):
        
        print(f"Product: {self.product}")
        print(f"Price per unit: ₹{self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Price: ₹{self.total_price()}")
        print(f"Discount: {self.discount_percent}%")
        print(f"Final Price after Discount: ₹{self.final_price()}")    

# Function Instance calling

ord = discount_order("Mango",200,3,20)
ord.display_order()       
            
        