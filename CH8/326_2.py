# client
import socket;

host=socket.gethostname()
port=4545
a=(host,port)
client_socket=socket.socket()
client_socket.connect(a)


while True:
    message=input("=>")
    if message==" ":
        break
    client_socket.send(message.encode())
    ans=client_socket.recv(1024).decode()
    print(ans)
     
client_socket.close()