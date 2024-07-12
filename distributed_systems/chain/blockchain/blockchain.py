import hashlib
import time
from flask import Flask, request, jsonify
import requests

phases = ""
class Block:

    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.hash = self.calculate_hash()
 
    def calculate_hash(self):
        global phases
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.transactions}"
        return hashlib.sha256(block_string.encode()).hexdigest()
 
class Blockchain:
    def __init__(self):
        global phases
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        phases += "constructor - "
 
    def create_genesis_block(self):
        global phases
        phases += f"create_genesis_block - "
        return Block(0, "0", [])
        
 
    def get_latest_block(self):
        global phases
        phases += "create_genesis_block - "
        return self.chain[-1]

    def add_transaction(self, transaction):
        global phases
        self.pending_transactions.append(transaction)
        phases += f"add_transaction - {self.pending_transactions}"
        #cerrar BLOQUE
        self.openCloser(self.pending_transactions)
        return jsonify({"message":f"{self.pending_transactions}"})
 
    def openCloser(self, transaction):
        global phases
        data = transaction
        phases += f"openCloser -> {data}"
        #get_json()
        response = requests.post('http://closerblock:5004/close_block', json=data)
        if response.status_code == 200 and response.json().get('message') == 'Close block':
            #aquí se llama al endpoint
            self.close_block()
        else: 
            pass
 
    def create_block(self):
        global phases
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, self.pending_transactions)
        self.pending_transactions = []
        phases += f"create_block - "
        self.chain.append(new_block)
        
 
    def close_block(self):
        global phases
        phases += "close_block - "
        self.create_block()
 
app = Flask(__name__)
blockchain = Blockchain()
 
@app.route('/register_tx', methods=['POST'])
def register_tx():
    global phases
    data = request.get_json()
    blockchain.add_transaction(data)
    return jsonify({'message': phases}), 201
 
@app.route('/close_block', methods=['POST'])
def close_block():
    global phases
    blockchain.close_block()    
    return jsonify({'message': phases}), 201

@app.route('/searchMethods', methods=['GET'])
def searchMethods():
    global phases
    return phases
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

