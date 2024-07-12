from flask import Flask
from flask import jsonify
from flask import request
from time import sleep
from urllib import response
import requests
import json

app = Flask(__name__)

#Fuse----

vecinos=[
 {
 'ip':'172.17.0.3', # n2
 'port':'2001'
 },
 {
 'ip':'172.17.0.9', # n8
 'port':'2007'
 }
 ]

cpvecinos = vecinos.copy() # COPIA DEL DICCIONARIO VECINOS
ipPort = {}
ipfather = None
ph = [
    {'7': 'Nodo 5: todos los hombres vuelven a ser hermanos'}
    ]
vecinos_iter = None # datos de hijos a iterar 🦠 MODIFICAR

# Nodo 5: Frase7 = "todos los hombres vuelven a ser hermanos"
@app.route('/nodo/getPhrase',methods=['GET'])
def getPhrase():
    return jsonify(ph)

#ip del host
def ip():
    return {'ip': "172.17.0.6", 'port':'2004'}


# 🦠 MODIFICAR
@app.route('/nodo/iniciar', methods=['POST'])
def iniciar():
    global cpvecinos
    global vecinos_iter
    vecinos_iter = iter(cpvecinos) #variable glovbal a iterar
    iniciarPropagar()
# SOLO SIRVE PARA EL NODO GENESIS
def iniciarPropagar():
    global cpvecinos
    global vecinos_iter
    try:
        hijo = next(vecinos_iter) # importante
        print(f"el valor de vecino es: {hijo}")
        ipHijo, portHijo = hijo.values()
        print(f"el valor que adquirió ipHijo es: {ipHijo} y el valor de portHijo {portHijo}")
        ipPort = ip() # enviar ip de padre a sus hijos 
        requests.post(f"http://{ipHijo}:{portHijo}/nodo/getIPFather", data = json.dumps(ipPort))
        iniciarPropagar()
    except StopIteration:
        sleep(30)
        return getPhrases()

#SIRVE PARA TODOS LOS DEMÁS NODOS
def propagar():
    global ph
    global cpvecinos
    global vecinos_iter # Solo itera los hijos, no al padre
    if len(ph)==8:
        getPhrases()
    else:
        try:
            hijo = next(vecinos_iter)
            print(f"el valor de vecino es: {hijo}")
            ipHijo, portHijo = hijo.values()
            print(f"el valor que adquirió ipHijo es: {ipHijo} y el valor de portHijo {portHijo}")
            ipPort = ip() # enviar ip de padre a sus hijos 
            requests.post(f"http://{ipHijo}:{portHijo}/nodo/getIPFather", data = json.dumps(ipPort))
            propagar()
        except StopIteration:
            return # YA TERMINÓ PORQUE NO HAY MÁS VECINOS
# 🦠 MODIFICAR


# aquí se recibe la ip que se envia en el metodo propagar
@app.route('/nodo/getIPFather', methods=['POST'])
def getIPFather():
    print("----- INICIALIZACIÓN  DE GETIPFATHER --------")
    global cpvecinos
    global ipPort
    global vecinos_iter
    #Validación que ip haya llegado bien - LUEGO PUEDES ELIMINAR -
    ipPort = json.loads(request.data.decode())  # dicciconario con ip y puerto
    print(f"llegó el diccionario: {ipPort}") # agregar en todos
    ipfather = ipPort['ip'] # ip del padre
    if ipfather != None:
        print(f"si llegó la ip del padre {ipfather}")
        print("Iniciando eliminación de padre en cpvecinos")
        cpvecinos = [vecino for vecino in cpvecinos if vecino["ip"] != ipfather]
        # 🦠 MODIFICAR
        vecinos_iter = iter(cpvecinos) # ITERA SOLO EN LOS HIJOS
        buscarVecinos()
    else:
        print(f"no llegó la ip del padre {ipfather}")
        exit()
    return 0

def buscarVecinos():
    global cpvecinos
    print("----- INICIALIZACIÓN  DE BUSCARVECINO --------")
    print(cpvecinos)
    if len(cpvecinos) > 0:
        print("Entró a propagar")
        sleep(3)
        propagar() #aún tiene varios vecinos
    else:
        print("ya salió de buscarVecinos a validar()")
        validar()
        
def validar():
    print("----- INICIALIZACIÓN  DE VALIDAR --------")
    global ph
    global cpvecinos
    global ipPort
    if len(cpvecinos) == 0:
        print("Ya puede responder a su padre")
        send = ph
        # 👿| agregar a todos y revisa cuando es el padre que no puede entrar a nada
        if not any('ip' in d for d in send):
            send.append({'ip': '172.17.0.6'}) #CAMBIA ESTO POR LA IP LOCAL DEL HOST
            print("👾")  
            try:
                requests.post(f"http://{ipPort['ip']}:{ipPort['port']}/nodo/addPhrase", data = json.dumps(send))
                getPhrases()
            except requests.exceptions.RequestException as e:
                return jsonify(error=str(e)), 400
        else:
            print("ya venia cargada, se procede a eliminar todos las ip previas")
            send = [d for d in send if 'ip' not in d]
            exit()
        # 👿|
    else:
        print("ha ocurrido un error")
        exit()

# AÚN FALTA AÑADIR EL MÉTODO ADDPHRASE Y EXIT()
@app.route('/nodo/addPhrase', methods=['POST'])
def addPhrase():
    print("----- INICIALIZACIÓN  DE ADDPHRASE --------")
    global ph
    global cpvecinos
    dataNodeHijo = json.loads(request.data.decode()) 
    ipHijo = [dic['ip'] for dic in dataNodeHijo if 'ip' in dic] #trae la ip del hijo
    cpvecinos = [vecino for vecino in cpvecinos if vecino["ip"] != ipHijo[0]] # borra la ip del diccionario 
    dataNodeHijo = [d for d in dataNodeHijo if 'ip' not in d] # borra el diccionario ip de dataNodeHijo que tiene las frases
    print(f"se ha borrado el hijo {ipHijo} y ahora el diccionario principal viene con {cpvecinos}")
    #añadir demás diccionarios a ph
    ph.append(dataNodeHijo)
    print(f"se han añadido las frases {ph}")
    buscarVecinos()
    return 0

def getPhrases():
    global cpvecinos
    global ph
    while len(cpvecinos) != 8:
        sleep(1)
        print("----- INICIALIZACIÓN  DE GETPHRASES --------")
        if len(ph) == 8:
            print("Ya tiene las 8 frases")
            ph = sorted(ph, key=lambda x: list(x.keys())[0]) #organizar
            print(f"Se ha organizado y terminó {ph}")
            
        else:
            print("Aún no completa las 8 frases")
            exit()
            
    return ph



if __name__ == '__main__':
 app.run(host="172.17.0.6", port=2004)
