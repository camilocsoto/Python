import functools as fc
import random
class Array():
    """ 
    Array vs ArrayLists
    son listas... pero las listas no son arrays.
    no ocupan mucho espacio en la ram.
    los arrays son más estáticos, solo puedeen:
    -crearse
    -medir su longitud.
    -represtarse en strings
    -pertenencia
    -índices
    - reemplazos
    """
    def __init__(self, sizes, fill_values=None):
        self.items =list()
        #create the values from the size
        for _ in range(sizes):
            self.items.append(fill_values)
    
    def __len__(self): #a convention to private methods 
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
        return self.items[index]
    
    def __generate__(self):
        for i in range(len(self.items)):
            self.items[i-1] = random.randint(1,100)
        return self.items
    
    def __sum__(self):
        reduced = fc.reduce(lambda x,y : x+y, self.items)
        return reduced
    
if __name__=="__main__":
    menu = Array(3)
    print(menu.__len__())
    print(menu.__generate__())
    print(menu.__sum__())
    print(menu.__setitem__(0, "2"))

    
    
    
    
    