import xmlrpc.client
import socket
import functools

#----------------------------------------------------------------------------
class Client:
    def __init__(self, name, ipServerIndex):
        #Server index IP
        if(ipServerIndex==""):
                self.indexIP='172.17.0.2'
        else:
                self.indexIP=ipServerIndex

        self.clientsList={} #clients ips and names
        self.array_nums_hosts=[] #arreglo de numeros aleatorio para cada cliente
        self.data={} #ip y array unidos en un diccionario
        self.clientIP=str(socket.gethostbyname(socket.gethostname()))
        self.name=name
        self.arrayClient = []#numeros del cliente respectivo
        self.status = False

    #get clients list from serverClient        
    def getClientsList(self):
        s = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        self.clientsList=s.getClientsList()


    #Send messages to all client partners
    def sendMessage(self, txt):
        #update clientsList
        self.getClientsList()
        #Send message to all clients
        for key in self.clientsList:
            IPClient = self.clientsList.get(key)
            s = xmlrpc.client.ServerProxy('http://'+str(IPClient)+':8000')
            s.receiveMessage(self.name,txt)

    #Show all received messages from others clients
    def showReceivedMessages(self):
        s = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        return s.getReceivedMessages()

    #Register client in the serverIndex
    def registerMe(self):
        sIndex = xmlrpc.client.ServerProxy('http://'+self.indexIP+':8000')
        sIndex.register(self.clientIP, self.name)

    #traigo los numeros del servidor de este cliente
    def getNumsHost(self):
        s = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        self.array_nums_hosts=s.getNumsHost()
        print("nuemros sin ip del servidor cliente")
        print(self.array_nums_hosts)
        return self.array_nums_hosts
    
    #registrar numeros del cliente en un diccionario con la Ip del cliente
    def keep_data(self):
          print("se totoea")
          nums = self.getNumsHost()
          self.data[self.clientIP] = nums
          #self.data[self.getNumsHost()] = self.clientIP
          #self.data[self.clientIP] = self.getNumsHost()
          print(self.data)
          print("metodo keep trae el diccionario con ip y numeros")
          print(self.clientIP)
          print(self.data)
          #self.envioNumeros()
          self.enviodiccionarioIndex()
          return self.data

      #hay que mandar este diccionario con la ip y los numeros al index, luego el index lo guarda y se consultan no del servidor
        #cliente porque se borra si no del index que guarda lo de cada servidorcliente y asi se cree otro cliente su servidor
        #sirve como mediador de generar el diccionario con la informacion y enviarlo al index, que contendra todas las ip y numeros y luego
        #toca traer esa informacion denuevo del index al servidor cliente y mandarlo al cliente y imprimirlo
              
              
    #Envio el diccionario con su ip y numeros al index para que los almacene
    def enviodiccionarioIndex(self):
        nums = self.getNumsHost()
        print("entro metodo para enviar datos al index")
        for key, nums in self.data.items():
              sIndex = xmlrpc.client.ServerProxy('http://'+self.indexIP+':8000')
              sIndex.guardarDiccionario(key,nums)

       
    #resivo los numeros con la ip del servidor cliente que fueron enviados por el index
    def recibir(self):
        s = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        self.data=s.getNumsHostComplete()
        self.obtenerArrayDeNumeros(self.data)
        print(self.data)#esta vacio
    #----------------------------------------------------------------------------------------------------
    def obtenerArrayDeNumeros(self, diccionary):
        print("entro al obtener array de nums y el diccionario es:")
        print(diccionary)
        for key, value in diccionary.items():
                IpClients = key
                if self.clientIP== IpClients:        
                        self.arrayClient = value
        print(self.arrayClient)
        self.ejecutarProgram() # 🟠

    def ejecutarProgram(self):
        
          if len(self.clientsList) >=3:
                print("iniciando algoritmo...")
                self.validar_orden_cliente()
          else:
                print("espere a que se conecten los demás clientes...")
        
          self.validar_orden_cliente()

    def validar_orden_cliente(self):
        print("entró a validar el orden del host local"*4)
        print("arreglo original del cliente")
        elementos_repetidos = list(filter(lambda x:  self.arrayClient.count(x) > 1, range(11)))
        print("nums repetidos de array -> "+ str(elementos_repetidos))

        if (len(elementos_repetidos) ==0) :
              print(f'el pc {self.clientIP} ya está organizado')
              self.status = True
        else:
                print(f'el pc {self.clientIP} no está está organizado')
                self.negociar()
              

    def armar_diccionario(self, ip):
        cpArrayClient = self.data[ip] #array de numeros no repetidos para el diccionario
        repetidos = [] #array de numeros repetidos para el diccionario
        nums_faltantes = list(filter(lambda num: num not in cpArrayClient, range(11))) # 🟢
        #ciclo para crear lista de numeros repetidos y eliminar de la copia los repetidos.
        while True:
                print("CViclo whiule")
                auxiliar =[]
                repited_nums_temp = list(filter(lambda x:  cpArrayClient.count(x) > 1, range(11)))
                if len(repited_nums_temp)==0:
                      break
                else:
                      auxiliar.extend(repited_nums_temp)
                      repetidos.extend(repited_nums_temp) # 🟢
                      for num in auxiliar:
                        if num in cpArrayClient:
                                cpArrayClient.remove(num)
        send_dictionary = {
                'ip':ip,
                'nums':cpArrayClient,
                'nums_faltantes':nums_faltantes,
                'nums_repetidos': repetidos
        }
        return send_dictionary


    def negociar(self):
        client1 = self.armar_diccionario(self.clientIP)
        print(f'se armó el diccionario cliente -> {client1}')
        for key in self.data.items():
                print("ciclo feo")
                IpClients = key
                print(f'key->{key}')
                yield key
                
                client2 =  self.armar_diccionario(IpClients)
                if(len(client2['nums_repetidos'])>0):
                        print("ambos clientes deben negociar")
                        sc = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
                        sc.getClientsDictionaries(client1, client2)
                        self.reescribir()
                        next(key)
                else:
                     print("ordenado")
                     break

    def reescribir(self):
        sc = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        self.data=sc.send_new_nums() # esto no es permitido pero debo esperar a que la función deje de ser null
        self.obtenerArrayDeNumeros(self.data)
        self.enviodiccionarioIndex()
        print(f'se supone que, {self.data} ya está actualizado en todos los host')#esta vacio
        return 0

#se creo metodo para guardar array de la ip 
#se creo negociacion con los otros clientes
#reorganiza se optiene el arreglo del clietne actual y el arreglo siguietne cliente
    

    
        
     
if __name__ == "__main__":
      client=Client(input("Client name: "), input("Index Server IP (172.17.0.2): "))
      client.registerMe()
      client.keep_data()#llamo al metodo

      print("empezando")
      client.recibir()
      
      print("terminó")
      print(client.data)
"""

#----------------------------------------------------------------------------

#Terminal--------------------------------------------------------------------
client=Client(input("Client name: "), input("Index Server IP (172.17.0.2): "))
client.registerMe()
client.keep_data()#llamo al metodo
client.recibir()
while(True):
        #client1.showReceivedMessages()
        command=input(client.name+"::. ")
        if(command=="bye"):
                break
        elif(command=="send message"):
                client.sendMessage(input("message>>"))
        elif(command=="show received messages"):
                print(client.showReceivedMessages())
        elif(command=="get clients list"):
                client.getClientsList()
                print(client.clientsList)
        elif(command=="help"):
                print("send message: send a message to all clients")
                print("get clients list: show the clients list")
                print("bye: exit")
                print("help: show commands and its explanation")
        elif(command=="list"):
                client.recibir()
                print(client.recibir)
        else:
                print("command not found")     
#----------------------------------------------------------------------------

"""


