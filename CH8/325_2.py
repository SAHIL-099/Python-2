# clinet
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
    print(reply.decode())
    
udp_client.close()