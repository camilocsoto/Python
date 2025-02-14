"""_summary_
    los decoradores permiten añadir funcionalidad a una función sin modificar su código
    - principio Open/Closed
    - patrón de decoradores. ♾️
    Returns:
        _type_: function wrapper
"""
#decorador a invocar sin parametros
def log_transaction(func):
    def wrapper():
        print(f'logging transaction for {func.__name__}') #1
        func()
        print(f'transaction for {func.__name__} logged') #3
    return wrapper

@log_transaction
def proccess_payment():
    """_summary_
    se pretende añadir funcionalidad que va a ser común a todas las funciones que se le aplique el decorador
    """
    print('stripe payment process...') #2
    
proccess_payment()

# decorador a invocar con parametros
def check_access(func):
    def wrapper(employe): # obtiene los parametros de la función
        if employe.get('role') =='admin':
            return func(employe) #1: llama a delete_employee que recibió el decorador.
        else:
            print("you cannot erase this user.")
    return wrapper

@check_access
def delete_employe(employe):
    print(f'{employe} deleted') #2 
    
employe = {'name':'Juan', 'role':'admin'}
delete_employe(employe)


