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
        # |
        # v muestro los numeros del servidor cliente con la ip y los numeros
        def getNumsHostComplete(self):
            print("metodo hostcomplete ")
            print(self.data) #vacio
            return self.data
        
        def getClientsDictionaries(self, client1, client2):
            print("entró al serverClient y recibió los diccionarios.")
            print(f'antes -> client1_{client1} y client2_{client2}')
            self.negociar_numeros(client1, client2)
            return 0
            
        def negociar_numeros(self, client1, client2):
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
            self.actualizar_nuevos_numeros(client1, client2)
        
        def actualizar_nuevos_numeros(self, client1, client2):
            print("actualizará numa en self.data")
            for ip in self.data:
                if client1['ip'] == ip:
                    self.array_nums_hosts = client1['nums']
                    print(f'diccionario data se actializó en su ip {ip}, y terminó con el array: {self.data[ip]}')
                elif client2['ip'] == ip:
                    print(f'diccionario data se actializó en su ip {ip}, y terminó con el array: {self.data[ip]}')
                    # enviar al otro cliente su nuevo array.
            # borrar datos de los diccionarios
            client1 = {}
            client2 = {}
            print("terminó de actualizar")
            return 0

        def send_new_nums(self):
            print("el metodo reescribir se está ejecutando y solcito la función send_new_nums")
            print(self.data)
            return self.data
        
        def guardarNuevoDiccionario(self, newData):
            print("se guarda el nuevo diccionario en todos los hosts.")
            self.data = newData
            self.enviarClient()
            return 0
        
        def enviarClient(self):
            print("se actualiza a todos los clients desde servClient")
            return self.data
            
            
        
        #def enviar nuevo diccionario a todos los clientes
    #----------------------------------------------------------------------------
    server.register_instance(ServerClient())

    # Run the server's main loop
    server.serve_forever()
