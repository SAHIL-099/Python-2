# Write a Python program to build a TCP host server that accepts a message from clients and returns the same message to the client. Write 
# programs for both the server and client side

# server

import socket;

host=socket.gethostname()
port=4545
a=(host,port)

server_socket=socket.socket()
server_socket.bind(a)
server_socket.listen()
conn,add=server_socket.accept()

while True:
    data=conn.recv(1024).decode()
    if data==" ":
        break
    conn.send(data.encode())
    
server_socket.close()
    