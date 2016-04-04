import socket
#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 82))
#become a server socket
serversocket.listen(5)
conn, addr = serversocket.accept()
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
