import socket

server = socket.socket()

server.bind(("localhost", 5000))

server.listen(1)

print("Server is waiting...")

client, address = server.accept()

print("Client connected:", address)

message = client.recv(1024).decode()

print("Client says:", message)

client.send("Hello Client".encode())

client.close()
server.close()