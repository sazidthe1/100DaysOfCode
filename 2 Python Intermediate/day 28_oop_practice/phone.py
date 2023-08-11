from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Calling super function to access all the attributes / methods
        super().__init__(name, price, quantity)

        # Run validation to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} can't be less than or equal to Zero!"

        # Assign to self object
        self.broken_phones = broken_phones