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
          sentence = connectionSocket.recv(1024).decode()
          print("received message is: ", sentence)
          capitalizedSentence = sentence.upper()
          if(capitalizedSentence=="EXIT"):
               connectionSocket.send(capitalizedSentence.encode())
               print("reply sent, server socket closed")
               connectionSocket.close()
               break
          messagelen = str(len(capitalizedSentence))
          connectionSocket.send(messagelen.encode())

     
