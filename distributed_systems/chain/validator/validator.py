from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/validar_tx', methods=['POST'])
def validar_tx():
    data = request.get_json()
    # Implement validation logic here
    
    # Claves requeridas
    claves_requeridas = ['dir1', 'dir2', 'monto']
    
    # Verificar si todas las claves requeridas están en el diccionario
    for clave in claves_requeridas:
        if clave not in data:
            return jsonify({'message': f"Falta la clave: {clave}"}), 400

    # Verificar tipos de datos
    if not isinstance(data['dir1'], str):
        return jsonify({'message': "El valor de 'dir1' debe ser una cadena"}), 400
    
    if not isinstance(data['dir2'], str):
        return jsonify({'message': "El valor de 'dir2' debe ser una cadena"}), 400
    
    try:
        monto = float(data['monto'])
    except ValueError:
        return jsonify({'message': "El valor de 'monto' debe ser un número"}), 400

    # Si todas las verificaciones pasan
    return jsonify({'message': 'Transaction validated'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)