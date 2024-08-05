# Write a Python program to build Simple HTTP Server in Python



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
    print(data)
    ans=input("=>")
    conn.send(ans.encode())
    
server_socket.close()
    