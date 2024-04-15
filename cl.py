# Import socket module
import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 

print("Diffie Client Side \n")
P=int(input("Enter P(prime number:) "))
G=int(input("Enter G(primitive root of P:) "))
s.sendall(str.encode("\n".join([str(P), str(G)])))
a=int(input("Enter the private key:"))
#Key generation
x=(G**a)%P
y=int((s.recv(2048)).decode('utf-8'))
#Secret Key
ka=(y**a)%P
print("Secrey Key ka is:",ka)
s.sendall(str.encode("\n".join([str(x), str(ka)])))
#print("Recieved encrypted message is = ",k)
s.close()
