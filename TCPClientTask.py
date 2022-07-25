from socket import *
serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
while 1:
    sentence = input('Enter message to sent or type Exit to disconnect: ')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    if(modifiedSentence.decode()=="EXIT"):
        print('received messsage from the server: Disconnect')
        print("now you are disconnected from the server")
        break
    servermessage= "your data was "+modifiedSentence.decode()+" bytes"
    print ("received message from server: ",servermessage)

