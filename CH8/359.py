# Write a Python program to build a UDP localhost host server that accepts a number 
# from client and returns the square of that number to the client. (write server side program 
# only)

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
    num=int(data.decode())
    sq=num*num
    ans=str(sq)
    udp_server.sendto(ans.encode(),addr)
    
    
udp_server.close()