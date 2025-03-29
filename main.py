import socket

s = socket.socket()
s.bind(('', 8000))

s.listen()

print('Awaiting connections from the Node.js server...')

while True:
    conn, address = s.accept()
    print(f'Connected to {address}')

    try:
        data = conn.send(b'The socket connection works as expected!')
        conn.close()
    except Exception:
        print('Something went wrong!')