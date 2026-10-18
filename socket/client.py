import socket

client = socket.socket()

client.connect(("localhost", 5000))

client.send("Hello Server".encode())

message = client.recv(1024).decode()

print("Server says:", message)

client.close()