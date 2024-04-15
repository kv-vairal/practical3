import socket
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")

port = 12345               
 
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")    
while True:
    c, address = s.accept()
    P, G = [int(i) for i in c.recv(2048).decode('utf-8').split('\n')]
    print("Recieved public keys from client is P,G", (P,G))
    b=int(input("Enter the private key:"))
    #Key generation
    y=(G**b)%P
    c.send(str(y))
    x, ka = [int(i) for i in c.recv(2048).decode('utf-8').split('\n')]
    print("Recieved x and ka from client", (x,ka))
    #Secret Key
    kb=(x**b)%P
    print("Secrey Key ka is:",kb)
    if ka==kb:
        print("Secret Keys shared are same")
    else:
        print("Secret Keys are not same")
    
    c.close()
