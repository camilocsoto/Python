from flask import Flask, request, jsonify
import requests, ast

app = Flask(__name__)

phases = []
 
@app.route('/close_block', methods=['POST'])
def close_block():
    global phases
    data = request.get_json()
    phases.append(data)
    # Obtener el valor de 'phases'
    phases = data['phases']
        # Contar el número de listas en phases
    num_lists = len(phases)
    if len(num_lists) == 3:
        message = "Close block"
    else:
        message = "Continue"

    return jsonify({'message': message}), 200
    
@app.route('/search', methods=['GET'])
def search():
    global phases
    return jsonify({'phases': phases})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)