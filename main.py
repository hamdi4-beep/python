import socket

# creates a socket object
s = socket.socket()
s.bind((socket.gethostname(), 3000))

s.listen(1)

while True:
    (client, address) = s.accept()
    print(client.recv(1024))