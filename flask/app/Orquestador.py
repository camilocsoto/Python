from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obtener_tienda', methods=['POST', 'GET'])
def obtener_tienda():
    
    try:
        response = requests.get('http://localhost:5002/obtener_tienda')
        print(response.status_code)
        if response.status_code == 200:
            datos = response.json()
            print(datos)
            return jsonify(datos)
    except Exception as e:
        print(e)
    

"""
@app.route('/agregar_nuevo_producto', methods=['POST'])
def agregar_nuevo_producto():
    datos_nuevo_producto = {
        'nombre': "Silla de jardin",
        'cantidad': 20,
        'precio': 150
    }
    resultado = agregar_producto(datos_nuevo_producto)
    return jsonify(resultado)
"""


if __name__ == "__main__":
    app.run(debug=True, port=5000)