from flask import Flask, request, jsonify

app = Flask(__name__)

productos = [
    {'nombre': "Silla de comedor", 'cantidad': 20, 'precio': 150},
    {'nombre': "Librero", 'cantidad': 7, 'precio': 500},
    {'nombre': "Escritorio", 'cantidad': 8, 'precio': 800},
    {'nombre': "Cama King Size", 'cantidad': 3, 'precio': 1500},
    {'nombre': "Mesa de noche", 'cantidad': 10, 'precio': 200},
    {'nombre': "Armario", 'cantidad': 4, 'precio': 1200}
]

def obtener_lista_productos():
    return productos

@app.route('/obtener_tienda', methods=['GET'])
def obtener_tiendas():
    lista_productos = obtener_lista_productos()
    return jsonify(lista_productos)

@app.route('/agregar_productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = request.json
    for producto in productos:
        if producto['nombre'] == nuevo_producto['nombre']:
            producto['cantidad'] += nuevo_producto['cantidad']
            return {"message": "Cantidad actualizada para el producto existente"}
    # Si el producto no existe, se agrega a la lista
    productos.append(nuevo_producto)
    return {"message": "Producto agregado exitosamente"}

if __name__ == "__main__":
    app.run(port=5002)
