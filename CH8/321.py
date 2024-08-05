# write a Python program to build a UDP client-side program

import socket;

host=socket.gethostname()
port=4040
a=(host,port)
udp_client=socket.socket(type=socket.SOCK_DGRAM)

while True:
    data=input("=>")
    if data=="":
        break
    udp_client.sendto(data.encode(),a)
    reply,addr=udp_client.recvfrom(1024)
    print("repl is ",reply.decode(),"from addr",addr)
    
udp_client.close()