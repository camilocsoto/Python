from vectors1D import Array
from random import randint
class BiArray():
    """ 
    2D Array
    U can do the same than the 1D arrays
    los métodos dunder (__getitem__, __setitem__, etc.) 
    permiten sobrecargar operadores para acceder a elementos 
    de estructuras de datos de manera intuitiva usando corchetes ([]). 
    
    La notación vector[1][1] primero llama a vector.__getitem__(1), que 
    devuelve una instancia de Array, y luego llama a __getitem__(1) en 
    esa instancia, accediendo así al elemento deseado. Esta capacidad de 
    anidación es eficiente y facilita el acceso a datos multidimensionales.


    """
    def __init__(self, columns, rows, fill_values=None):
        self.items =Array(rows) #1 dimension and recive the nums... arrays.py
        for y in range(rows):
            self.items[y] = Array(columns, fill_values)
    
    def get_height(self):
        return len(self.items)
    
    def get_width(self): 
        return len(self.items[0]) # the horizontal is always 0
    
    def __getitem__(self, index):
        return self.items[index]
    
    
    def __asign__(self):
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                self.items[y][x]=randint(1,100)
        
        return str(self.__str__())
    
    def __str__(self):
        result = ""
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                result += str(self.items[y][x]) +" "
            result +="\n"
        return str(result)
    
if __name__=="__main__":
    vector = BiArray(3,4)
    print(f"{vector.get_height()} it should give you 3")
    print(f"{vector.get_width()} it should give you 4")
    print(f"BEFORE_ {vector.__str__()} ")
    print(f"AFTER_ {vector.__asign__()} ")
    print(f"{vector.__getitem__(0)[0]} ")
    
    