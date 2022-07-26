from socket import *
import sys

serverIP = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
firstnum=sys.argv[1]
operator = sys.argv[2]
secondnum=sys.argv[3]


clientSocket.bind(('',0))

clientSocket.sendto(firstnum.encode(), (serverIP, serverPort))
clientSocket.sendto(operator.encode(),(serverIP,serverPort))
clientSocket.sendto(secondnum.encode(),(serverIP,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())

clientSocket.close()

