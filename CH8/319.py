# write a python program to build a udp server side program

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
    print("message is",data,"addr is:",addr)
    ans=input("=>")
    udp_server.sendto(ans.encode(),addr)
    
    
udp_server.close()