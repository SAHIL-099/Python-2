# Write a Python program to build a UDP host server that accepts a message from clients and returns the same message to the client. Write 
# programs for both the server and client side.

# server

import socket;
host=socket.gethostname()
port=4040
a=(host,port)
udp_server=socket.socket(type=socket.SOCK_DGRAM)
udp_server.bind(a)

while True:
    data,addr=udp_server.recvfrom(1024)
    if(data.decode()==""):
        break
    ans=data.decode()
    udp_server.sendto(ans.encode(),addr)
    
    
udp_server.close()