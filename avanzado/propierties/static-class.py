
#staticmethod
class Order:

    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount*(tax_rate/100)


Order.calculate_tax(100, 18)

print(Order.calculate_tax(100, 18))

#classmethod
class Order2:
    discount = 10 #atrub global.
    
    def __init__(self, amount):
        self.amount = amount
    @classmethod
    def edit_discount(cls, edit_discount)
        cls.