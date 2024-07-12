from flask import Flask, request, jsonify
import requests
 
app = Flask(__name__)
 
@app.route('/process_transaction', methods=['POST'])
def process_transaction():
    data = request.get_json()
    # Validate transaction here
    response = requests.post('http://blockchain:5000/add_transaction', json=data)
    return jsonify(response.json()), response.status_code

#recive transaction
@app.route('/register_tx', methods=['POST'])
def register_tx():
    data = request.get_json()
    response = requests.post('http://validator:5003/validar_tx', json=data)
    if response.status_code == 200 and response.json().get('message') == 'Transaction validated':
        response = requests.post('http://blockchain:5000/register_tx', json=data)
        return jsonify({'message': 'Transaction blockchain verificated and added'}), 200
    
    else:
        return jsonify({'message': 'Transaction failed'}), 400

 
@app.route('/consult_funds', methods=['GET'])
def consult_funds():
    address = request.args.get('address')
    response = requests.get(f'http://blockchain:5000/consult_funds?address={address}')
    return jsonify(response.json()), response.status_code

@app.route('/index', methods=['GET'])
def index():
    putos = "putos middileware"
    return putos

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

