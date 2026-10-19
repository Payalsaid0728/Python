import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))

server.listen(1)

print("Server waiting for connection...")

client, address = server.accept()

print("Connected:", address)

message = client.recv(1024).decode()
print("Client:", message)

client.send("Hello from Server!".encode())

client.close()
server.close()