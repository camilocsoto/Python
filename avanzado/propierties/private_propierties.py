from dataclasses import dataclass

class BaseClass():
    __private_propierty:str = "I'm private"
    _protected_propierty:str = "I'm protected"
    public_propierty:str = "I'm public"
    
    def public_method(self):
        return self.public_propierty
    
    def _protected_method(self):
        return self._protected_propierty
    
    def __private_method(self):
        return self.__private_propierty

base = BaseClass()
print(base.public_method())
print(base._protected_propierty)
print(base.___private_method())