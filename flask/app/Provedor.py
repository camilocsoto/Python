import requests

# Definir los datos del nuevo producto
nuevo_producto = {'nombre': "Silla de jardín", 'cantidad': 15, 'precio': 200}

# Realizar la solicitud POST para agregar el nuevo producto
response = requests.post('http://localhost:5002/agregar_producto', json=nuevo_producto)

# Verificar el estado de la solicitud
if response.status_code == 200:
    print("Producto agregado exitosamente")
else:
    print("Error al agregar el producto:", response.text)