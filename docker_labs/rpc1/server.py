from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import socket
import random

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
# Create server
hostIP=str(socket.gethostbyname(socket.gethostname()))
with SimpleXMLRPCServer((hostIP, 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class Index:
        

        def __init__(self)->None:
            self.registeredList={} #clients ips and names
            self.array_nums_hosts = []

        #Register a client
        def register(self, ip, name):
            self.registeredList[name]=ip
            #Send clients IP to all clients
            self.sendRegisteredClientsList()
            self.create_nums()
            return self.registeredList

        #Send registered clients list to all clients
        def sendRegisteredClientsList(self):
            print("Clients List de func sendRegisterClientesList:")
            print(self.registeredList)
            cpRegisteredList=self.registeredList
            for key in self.registeredList:
                IPClient = self.registeredList.get(key)
                sc = xmlrpc.client.ServerProxy('http://'+IPClient+':8000')
                sc.updateClientsList(cpRegisteredList)
                

        def create_nums(self):
            # array that creates 44 nums from 0 to 10
            self.array_nums_hosts = list(range(11))*1
            #disorganize the array
            random.shuffle(self.array_nums_hosts)
            self.allocate(self.array_nums_hosts)

        #here, the array starts to allocate in every client... this must run in new every conection
        def allocate(self, host):
            #takes the last 11 nums of the array array_nums_hosts
            host = self.array_nums_hosts[-11:]
            #remove the last 11 nums of the array array_nums_hosts
            del self.array_nums_hosts[-11:]
            print("array de numeros se ejecuta bien en el allocate: "+str(host))
            self.sendNumsClients(host)
            return 0

        def sendNumsClients(self, array):
            print(f'array entra en la funcion send... {array}')
            print(self.registeredList)
            for key in self.registeredList:
                IPClient = self.registeredList.get(key)
                sc = xmlrpc.client.ServerProxy('http://'+IPClient+':8000')
                sc.setNumsHost(array)


                
    server.register_instance(Index())

    # Run the server's main loop
    print("Server Index actived in: "+hostIP)
    server.serve_forever()