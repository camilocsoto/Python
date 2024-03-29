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
        
        #muestro los numeros del servidor cliente con la ip y los numeros
        def getNumsHostComplete(self):
            print("metodo hostcomplete ")
            print(self.data) #vacio
            return self.data
        
        #recibe de negocioacion los arrays a reorganizar
        def reorganizar(self, arrayCliente, arrayNegocio):
                print("ssssssssssssssssssssssss")
                print(arrayCliente)
                print(arrayNegocio)
                # se agregan los numeros faltantes de cada arreglo en las siguientes variables
                numeros_faltantes1 = list(filter(lambda num: num not in arrayCliente, range(11)))
                numeros_faltantes2 = list(filter(lambda num: num not in arrayNegocio, range(11)))
                # (lambda x: arrayCliente.count(x) > 1 and x not in elementos_repetidos, arrayCliente))
                """
                elementos_repetidos1 = list(filter(lambda x:  arrayCliente.count(x) > 1 not in arrayCliente, range(11)))
                elementos_repetidos2 = list(filter(lambda x:  arrayNegocio.count(x) > 1 not in arrayNegocio, range(11)))
                aux = [x,y for (x,y): in  <]
                """
                print("numeros faltantes en cada array:")


                print(numeros_faltantes1)
                print(numeros_faltantes2)

        
        
    #----------------------------------------------------------------------------
    server.register_instance(ServerClient())

    # Run the server's main loop
    server.serve_forever()