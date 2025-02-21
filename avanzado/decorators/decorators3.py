from dataclasses import dataclass
"""
@staticmethod: no altera la clase ni el objeto, solo es invocable.
@classmethod: el method puede modificar la clase, no un objeto en particular.
@property: Ejecutar un method como un atributo, no recibe argumentos y es un getter-setter
"""

class Calculator:
    @staticmethod
    def add(a:int, b:int)->int:
        return a + b

# -- classmethod --
class Counter:
    count=0
    @classmethod
    def increase(cls):
        cls.count+=1 # puede modificar la clase counter
Counter.increase()
Counter.increase()
print(Counter.count) # 2

# -- property --
@dataclass
class Circle:
    _radius:float
    @property
    def return_area(self) -> float:
        return (self._radius**2)*3.1416
    
    # -- getter & setter --
    @property
    def radius(self)->float: #get
        return self._radius
    
    @radius.setter
    def radius(self, value:float) -> float:
        if value<0:
            raise ValueError("Radius can't be negative")
        else:
            self._radius = value
    
circ = Circle(5)
print(circ.return_area) # No necesita los parentesis.
# setter
circ.radius = 10
print(circ.return_area) # 314.16
    