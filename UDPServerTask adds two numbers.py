from socket import *
import operator
ops={b"+":operator.add,b"-":operator.sub}
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print ("The server is ready to receive")

while True:
    firstnum, clientAddress = serverSocket.recvfrom(2048)
    operator,clientAddress=serverSocket.recvfrom(2048)
    secondnum,clientAddress=serverSocket.recvfrom(2048)
    ffirstnum=int(firstnum)
    ssecondnum=int(secondnum)

    print(" is received from", clientAddress)
    addednum = ops[operator](ffirstnum,ssecondnum)
    modifiedMessage=str(addednum)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)