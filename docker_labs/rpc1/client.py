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
        self.clientIP=str(socket.gethostbyname(socket.gethostname()))
        self.name=name

    #get clients list from serverClient        
    def getClientsList(self):
        s = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        self.clientsList=s.getClientsList()


    def getNumsHost(self):
        s = xmlrpc.client.ServerProxy('http://'+self.clientIP+':8000')
        self.array_nums_hosts=s.getNumsHost()
        print(self.array_nums_hosts)

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
#----------------------------------------------------------------------------

#Terminal--------------------------------------------------------------------
client=Client(input("Client name: "), input("Index Server IP (172.17.0.2): "))
client.registerMe()
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
                client.getNumsHost()
                print(str(client.getNumsHost))
        else:
                print("command not found")     
#----------------------------------------------------------------------------

