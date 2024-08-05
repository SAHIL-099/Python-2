# write a program for making HTTP requests with sockets in Python. Make a socket to receive the data from the link: “ 
# https://www.ljku.edu.in/lju-at-a-glance ”

import socket
host="ljku.edu.in"
port=80
a=(host,port)
client_socket=socket.socket()
client_socket.connect(a)
link="GET https://ljku.edu.in/lju-at-a-glance HTTP/1.0\r\n\r\n"
client_socket.send(link.encode())
while True:
    data=client_socket.recv(1024).decode()
    if len(data)<1:
        break

    print(data,end="")
  
client_socket.close()
