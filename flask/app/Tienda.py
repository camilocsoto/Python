from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/obtener_lista_productos_inventario', methods=['POST', 'GET'])
def Obtener_Lista_Productos():
    
    try:
        response = requests.get('http://localhost:5000/obtener_tienda')
        print(response.status_code)
        if response.status_code == 200:
            datos = response.json()
            print(datos)
            return jsonify(datos)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    app.run(port=5001)