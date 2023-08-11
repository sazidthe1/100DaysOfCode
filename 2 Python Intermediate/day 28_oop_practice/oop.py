class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} can't be less than or equal to Zero!"
        assert quantity >= 0, f"Quantity {quantity} can't be less than or equal to Zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return (self.price * self.quantity) * self.pay_rate
    
    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'
    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

''' print(item1.calculate_total_price())
print(item1.apply_discount())
print(item2.calculate_total_price())
print(item2.apply_discount()) '''

''' Printing the each item name, and price
for instance in Item.all:
    print(instance.name, instance.price) '''

print(Item.all)