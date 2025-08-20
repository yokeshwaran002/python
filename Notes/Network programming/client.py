import socket
s = socket.socket()
s.connect(('localhost', 12000))
s.send(b"Welcomet to python  ")
