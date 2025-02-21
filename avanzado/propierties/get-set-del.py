"""_summary_
    @property: deja crear métodos del mismo nombre, solo cambia el decorador.
    @classmethod: en product, registra en la clase la instancias creadas.
"""
from typing import List
from dataclasses import dataclass, field
@dataclass
class Employee():
    name:str
    _salary:int
    
    @property
    def salary(self): #getter
        return self._salary
    
    @salary.setter 
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        else:
            self._salary = value
    
    @salary.deleter
    def salary(self):
        del self._salary
        print("salary has been deleted")

def exec_emp():
    emp = Employee("John", 1000)
    #get
    print(emp.salary)
    #set
    emp.salary = 2000
    print(emp.salary)
    #del
    del emp.salary

@dataclass
class Product():
    name:str
    _price:float
    _stock: int
    
    _instances:List['Product'] = [] # agrega los objetos creados para poder hacer la sumatoria del stock
    
    def __post_init__(self):
        Product._instances.append(self) # el error llega hasta aquí.
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        else:
            self._price = value
    @price.deleter
    def price(self):
        del self._price
        print("price has been deleted")
        
    @classmethod
    def total_stock(cls):
        return sum(product._stock for product in cls._instances)
    
def exec_prod():
    prod = Product("Laptop", 1000, 10)
    prod2 = Product("TV", 2000, 1)
    print(f'total stock: {Product.total_stock()}')
    
    
# exec it:
if __name__ == "__main__":
    exec_emp()
    exec_prod()
    