import socket
from functools import reduce

def client_program():
    #host = socket.gethostname()  # as both code is running on same pc
    host=["172.17.0.2","172.17.0.3","172.17.0.4"]
    port = 5000  # socket server port number
    data_temp = []
    for ip in host:
        client_socket = socket.socket()  # instantiate
        data =""
        client_socket.connect((ip, port))  # connect to the server
        message = "getNumber" # again take input
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        client_socket.close()  # close the connection
        data_temp.append(data)

    #convertir todos los valores a entero en una función lambda.    
    get_nums = list(map(lambda x: int(x), data_temp))
    suma = reduce(lambda x, y:x+y, get_nums)
    print(suma)




if __name__ == '__main__':
    client_program()
