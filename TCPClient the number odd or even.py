from socket import *
serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
while 1:
    sentence = input('Enter the number to sent or type 1000000 to disconnect: ')
    try:
        number=int(sentence)
    except:
        print("please enter integer ")
        clientSocket.send(sentence.encode())
        continue
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    if(modifiedSentence.decode()=="1000000"):
        print('received messsage from the server: Disconnect')
        print("now you are disconnected from the server")
        clientSocket.close()
        break
    servermessage= "the number you sent is {} ".format(modifiedSentence.decode())
    print (servermessage)
