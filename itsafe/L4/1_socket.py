import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 1234))
server.listen(5)

input('Enter')