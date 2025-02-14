import os
# decorador que comprueba si un empleado tiene un rol específico
def checkaccess(requiered_role): #param: str = 'admin'
    def decorator(func): #func: log_action
        def wrapper(employee): #dict: employee
            if employee.get('role') == requiered_role:
                return func(employee) # se rompe aquí 
            else:
                print(f'you cannot erase this user. {employee.get("name")}')
        return wrapper
    return decorator
    
def log_action(func):
    def wrapper(employee):
        if os.path.exists('log.txt'):
            with open('log.txt', 'a') as file:
                file.write(f'11/11/2001 - {func.__name__} created {employee} \n')
        else: # no sé si cuando no existe el archivo, el anterior if ya lo crea. explicame
            with open('log.txt', mode='w') as file:
                file.write(f'1/1/1999 log created. \n 11/11/2001 - {func.__name__} created {employee}\n')
        print(f'logging done')
        return func(employee) # llama a delete_e
    return wrapper

"""decoradores anidados:
    - El primero, tiene la información del decorador de adentro
    - Primero, crea el decorador de afuera y luego el de adentro
"""
@checkaccess('admin')
@log_action
def delete_e(employee):
    print(f'delete employee {employee.get("name")}')
    
employee = {'name':'Juan', 'role':'admin'}
delete_e(employee) # delete employee Juan