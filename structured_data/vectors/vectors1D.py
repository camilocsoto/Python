from typing import Optional, List
from dataclasses import dataclass, field
import functools as fc
import random

@dataclass    
class Array():
    """ 
    Array vs ArrayLists
    son listas... pero las listas no son arrays.
    no ocupan mucho espacio en la ram.
    los arrays son más estáticos, solo puedeen:
    -crearse, medir su longitud, pertenencia, índices
    """
    sizes:int
    fill_values:Optional[int] =None
    item:List[Optional[int]] = field(default_factory=list)
    
    def __post_init__(self)-> None:
        self.item= [self.fill_values for _ in range(self.sizes)]
    
    def __len__(self)->int:
        return len(self.item)
    
    def __str__(self):
        return str(self.item)
    
    def __iter__(self):
        return iter(self.item)
    
    def __getitem__(self, index)->List[int]:
        return self.item[index]
        
    def __setitem__(self, index, value)->int:
        self.item[index] = value
        return self.item[index]
    
    def __generate__(self):
        self.item = [random.randint(1,100) for _ in range(self.sizes)]
        return self.item
            
    def __sum__(self) -> int:
        valid_therms = [x for x in self.item if x is not None]
        return fc.reduce(lambda x, y: x+y, valid_therms)

if __name__=="__main__":
    menu = Array(3)
    print(menu.__len__())
    print(menu.__generate__())
    print(menu.__sum__())
    print(menu.__setitem__(0, "2"))