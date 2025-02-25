
#staticmethod

class Order:
    
    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount*(tax_rate/100)

print(Order.calculate_tax(100, 18))

#classmethod
class Order2:
    
    discount = 10 #atrub global.
    
    def __init__(self, amount):
        self.amount = amount
        
    @staticmethod
    def check_amount(amount):
        if amount >= 50:
            print('valid amount')
        else:
            print('invalid amount')
    
    @classmethod
    def edit_discount(cls, edit_discount):
        cls.discount = edit_discount
        
    @classmethod
    def create_order(cls, amount):
        output = f'before: {amount} after: {amount - (amount*cls.discount/100)}'
        return output

# change the global sets.
Order2.edit_discount(20)
Order2.discount
Order2.check_amount(100)
print(Order2.create_order(100))

