from socket import *
import threading

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 1234))
server.listen(5)


def worker(client):
    while True:
        data = client.recv(2048)

        if data == 'exit':
            client.close()
            break
        print("Client : {0}".format(data))

        data= input()
        client.sendall(data.encode())

server = socket(AF_INET, SOCK_STREAM)
server.bind(("", 4321))
server.listen(100)

# we got a client
while True:
    client,addr = server.accept()
    t = threading.Thread(target=worker, args=(client,))
    t.start()
