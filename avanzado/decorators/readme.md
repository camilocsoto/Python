# metaprogramación:

1. **decorators:** Funciones que modifican otras funciones/clases sin alterar su código.  
2. **high level functions:** Funciones que reciben o devuelven otras funciones.  
3. **create dynamic classes:** Definir clases en tiempo de ejecución con type().  
4. **metaclass:** Clases que crean clases, personalizando su comportamiento.  
5. **reflexión e introspección:** Examinar/modificar objetos en tiempo de ejecución con getattr(), setattr(), etc.  

El orden es importante:  
- `__new__` crea y controla la instancia del objeto  
- `__init__` crea el constructor
```python
class MultiplierFactory():
    def __new__(cls, factor: int):
        print(f"Creando instancia del factor {factor}")
        return super(MultiplierFactory, cls.__new__(cls)) #modifica la clase

    def __init__(self, factor: int):
        print(f"inicializado el {factor}")
        self.factor = factor

    def __call__(self, factor: int) ->int:
        return number:int*self.factor

mult = MultiplayerFactory(5) #exec __new__ & __init__
result = mult(10) # exec __call__ 
```