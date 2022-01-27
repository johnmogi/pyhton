from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 4321))

while True:
    data = input('Send(c2) :> ')
    client.sendall(data.encode())

    if data == 'exit':
        print('leaving chat... ')
        client.close()
        break

    data = client.recv(2048)
    print(data)