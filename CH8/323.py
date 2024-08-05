# Write a Python program to build a UDP localhost host server that accepts a number from clients and returns the cube of that number to the 
# client.

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
    cube=num**3
    ans=str(cube)
    udp_server.sendto(ans.encode(),addr)
    
    
udp_server.close()