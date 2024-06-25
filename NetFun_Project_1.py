
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
#Prepare a sever socket
#---
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#---
while True:    
    #Establish the connection    
    print('Ready to serve...')   
    connectionSocket, addr = serverSocket.accept()          
    try:        
        #---
        message = connectionSocket.recv(1024).decode()   
        #---
        filename = message.split()[1]                         
        f = open(filename[1:])              
        #---
        outputdata = f.read()
        f.close()                      
        #---
        #Send one HTTP header line into socket        
        #---
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'       
        connectionSocket.send(header.encode())
        #---
        #Send the content of the requested file to the client       
        for i in range(0, len(outputdata)):                   
            connectionSocket.send(outputdata[i].encode())        
        connectionSocket.send("\r\n".encode())        
        connectionSocket.close()    
    except IOError:        
        #Send response message for file not found       
        #--- 
        header = 'HTTP/1.1 404 Not Found\n\n'
        connectionSocket.send(header.encode())
        response = '<html><body><center><h1>Error 404: File not found</h1></center></body></html>'
        connectionSocket.send(response.encode())
        #Close client socket  
        connectionSocket.close()          
        #---
serverSocket.close()
sys.exit()
#Terminate the program after sending the corresponding data