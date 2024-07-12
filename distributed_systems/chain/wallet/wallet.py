from flask import Flask, request, jsonify, render_template
import requests

 
app = Flask(__name__)
 
@app.route('/register_transaction', methods=['POST'])
def register_transaction():
    data = request.get_json()
    response = requests.post('http://middleware:5001/register_tx', json=data)
    return jsonify(response.json()), response.status_code
 
@app.route('/consult_funds', methods=['GET'])
def consult_funds():
    address = request.args.get('address')
    response = requests.get(f'http://blockchain:5000/consult_funds?address={address}')
    return jsonify(response.json()), response.status_code
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  