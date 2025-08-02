from dataclasses import dataclass, field
from typing import List
@dataclass
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
# print(base.___private_method())

# cuenta bancaria que usa un método protegido para actualizazr le saldo y un método privado para registrar las transacciones.
@dataclass
class BankAccount():
    _money:float = 0.0
    _transactions:List[str] = field(default_factory=list)
    
    # Método privado para registrar transacciones
    def __deposit(self, amount: float):
        self._transactions.append(f"Deposited {amount}")

    # Método protegido para actualizar el saldo
    def _update_money(self, amount: float):
        self._money += amount
        self.__deposit(amount)
        return f"money updated {self._money} & transactions {self._transactions}"

# Uso:
account = BankAccount()
print(account._update_money(100))