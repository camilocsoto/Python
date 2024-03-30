from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import socket

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
# Create server
hostIP=str(socket.gethostbyname(socket.gethostname()))
print (hostIP)
with SimpleXMLRPCServer((hostIP, 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    
    #----------------------------------------------------------------------------
    class ServerClient:
        def __init__(self):
            self.clientsList={}
            self.data={}
            self.array_nums_hosts=[]
            self.messages={}
            #dictionary of 1 client
            self.clientDictionary = {}
            self.clientDictionary2 = {}

        #Save all messages from others clients
        def receiveMessage(self, name,txt):
            #self.messages[name]=txt
            self.messages["message"+str(len(self.messages)+1)]={name:txt}
            return 0
        
        #obtain received messages (it is to client use only)
        def getReceivedMessages(self):
            return self.messages

        #Update clients list from index (it is to index server only)
        def updateClientsList(self, clientsList):
            self.clientsList=clientsList
            return 0
        #obtain clients list (it is to client use only)    
        def getClientsList(self):
            return self.clientsList
        
        #obtengo los numeros del servidor index sin la ip
        def setNumsHost(self, array_nums_hosts):
            self.array_nums_hosts = array_nums_hosts
            return 0
        #muestro los numeros del servidor index sin la ip
        def getNumsHost(self):
            return self.array_nums_hosts
        

        #actualizar lista de numeros del servidor con la ip y los numeros
        def actualizar(self, data): #tengo las ip y numeros
            self.data=data
            print("se envia el diccionario del cliente asu servidor")
            print(self.data)
            return 0
        
        #muestro los numeros del servidor cliente con la ip y los numeros
        def getNumsHostComplete(self):
            print("metodo hostcomplete ")
            print(self.data) #vacio
            return self.data
        
        def getClientsDictionaries(self, client1, client2):
            print("entró al serverClient y recibió los diccionarios.")
            print(f'antes -> client1_{client1} y client2_{client2}')
            
            common_nums = set(client1['nums_faltantes']).intersection(client2['nums_repetidos'])
            # Add common numbers to client1['nums'] and remove them from client1['nums_faltantes'] and client2['nums_repetidos']
            for num in common_nums:
                client1['nums'].append(num)
                client1['nums_faltantes'].remove(num)
                client2['nums_repetidos'].remove(num)

            # Find common numbers between client2['nums_faltantes'] and client1['nums_repetidos']
            common_nums = set(client2['nums_faltantes']).intersection(client1['nums_repetidos'])

            # Add common numbers to client2['nums'] and remove them from client2['nums_faltantes'] and client1['nums_repetidos']
            for num in common_nums:
                client2['nums'].append(num)
                client2['nums_faltantes'].remove(num)
                client1['nums_repetidos'].remove(num)
            print(f'después -> client1_{client1} y client2_{client2}')
            """
            client 1 = {'ip': '172.17.0.5', 
            'nums': [4, 1, 9, 0, 6, 7, 2, 8], 
            'nums_faltantes': [3, 5, 10], #1
            'nums_repetidos': [2, 7, 8]#2
            }
            client = 2{'ip': '172.17.0.4', 
            'nums': [5, 9, 8, 10, 4, 3, 0, 1], 
            'nums_faltantes': [2, 6, 7], #2
            'nums_repetidos': [0, 3, 10] #1
            }
                
            if client1['nums_faltantes'] in client2['nums_repetidos']:
                #Recorre en el diccionario cliente 1 y comparalo con el cliente 2, con las claves que señalo en el anterior if
                #Si al recorrer ambos array hay numeros en comun, necesito que agregues ese numero en comun a client1['nums']
                #luego, elimina el numero en comun de cliente2['nums_repetidos'] y elimina el numero en comun de cliente1['nums_faltantes']
                #que dando client1['nums'] con los numeros correctos del cambio y me lo imprimes

                #Luego hacerlo has lo inverso la condicion quedario client2['nums_faltantes'] in client1['nums_repetidos']:
                #haces el procedimiento que se explico anterior mente para al final tener client2['nums'] con los numeros correctos del cambio y me lo imprimes
                #eliminar y agregar
                """
            
            return 0






        
        
    #----------------------------------------------------------------------------
    server.register_instance(ServerClient())

    # Run the server's main loop
    server.serve_forever()