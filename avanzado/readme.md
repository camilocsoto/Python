# Uso de métodos  

`@staticmethod`: no altera la clase ni el objeto, solo es invocable por la clase.  

```python

class Order:

    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount*(tax_rate/100)

#Ejecutas la clase, no un objeto!
Order.calculate_tax()

```

`@classmethod`: no altera un objeto, solo es invocable por la clase.  
**uso:** Un atributo global de debe modificarse en toda la clase. Y NO INSTANCIAR UN ATRIBUTO PARA UN OBJETO!

```python
class Order2:
    discount = 10 #atrub global.
    
    @classmethod
    def edit_discount(cls, edit_discount):
        cls.discount = edit_discount

Order2.edit_discount(20)
print(Order2.discount)
```

## self vs cls  
self afecta al objeto, no a la clase. `any`
cls afecta a la clase, no al objeto. `@classmethod` | `@staticmethod`
