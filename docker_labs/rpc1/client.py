import xmlrpc.client
import socket

#----------------------------------------------------------------------------
class Client:
    def __init__(self, name, ipServerIndex):
        #Server index IP
        if(ipServerIndex==""):
                self.indexIP='172.17.0.2'
        else:
                self.indexIP=ipServerIndex

        self.clientsList={} #clients ips and names
        self.array_nums_hosts=[]
        self.data={}
        self.clientIP=str(socket.gethostbyname(socket.gethostname()))
        self.name=name

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
              IpClients = key
              print("variable ip")
              print(IpClients)
              print("variable arreglo")
              print(nums)
              sIndex = xmlrpc.client.ServerProxy('http://'+self.indexIP+':8000')
              sIndex.guardarDiccionario(key,nums)

       
    #resivo los numeros con la ip del servidor cliente que fueron enviados por el index
    def recibir(self):
        s = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        self.data=s.getNumsHostComplete()
        print(self.data)#esta vacio

          
#----------------------------------------------------------------------------

#Terminal--------------------------------------------------------------------
client=Client(input("Client name: "), input("Index Server IP (172.17.0.2): "))
client.registerMe()
client.keep_data()#llamo al metodo
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


