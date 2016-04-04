#/usr/bin/python
import socket

HOST = socket.gethostname()    # The remote host
PORT = 82           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True :
        s.sendall('Hello, world')
        data = s.recv(1024)        
        print 'Received', repr(data)
