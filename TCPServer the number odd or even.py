from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
     print("listening at: ", serverSocket.getsockname())
     connectionSocket, addr = serverSocket.accept()
     print("the server is now connected to: ",addr)
     print("the server connect between ",connectionSocket.getsockname()," and ",addr)
     while True:
          try:
               number =int(connectionSocket.recv(1024).decode())
          except:
               if(not(connectionSocket)):
                    break
               print("wrong entry please enter integer")
               continue
          if(number==1000000):
               connectionSocket.send("1000000".encode())
               print("reply sent, server socket closed")
               connectionSocket.close()
               break
          elif(number==0):
               connectionSocket.send("zero".encode())
          elif(number%2==0):
               connectionSocket.send("even".encode())
          else:
               connectionSocket.send("odd".encode())
