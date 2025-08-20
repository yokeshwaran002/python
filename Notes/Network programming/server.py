import socket
s = socket.socket()
s.bind(('localhost', 12000))
s.listen(1)
conn, _= s.accept(); print(conn.recv(1024).decode())
