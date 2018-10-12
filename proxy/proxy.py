#!/usr/bin/env python
from socket import socket, AF_INET, SOCK_STREAM
import time

import sys
def proxy_server(server_ip,port,conn,addr,data):
    try:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((server_ip, port))
        serverSocket.send(data)
        print("send to" + str(addr) + " with message: " + sentence)
        while True:
            response = serverSocket.recv(1024)
            if len(response) > 0:
                conn.send(response)
            else:
                break
        serverSocket.close()
        conn.close()
    except:
        serverSocket.close()
        conn.close()
        print('error in proxy_server!')
        sys.exit(1)
if __name__ == '__main__':
    print(sys.argv)
    listen_port = sys.argv[1]
    fake_ip = sys.argv[2]
    server_ip = sys.argv[3]
    #listen_port = "8080"
    #fake_ip = "127.0.0.1"
    #server_ip = "127.0.0.1"
    try:
        proxySocket = socket(AF_INET, SOCK_STREAM)
        proxySocket.bind(('', int(listen_port)))
        proxySocket.listen(1)
        print('The proxy is ready to receive')
    except:
        print('unable to initialize proxy!')
        sys.exit(3)
    while True:
        try:
            clientSocket, addr = proxySocket.accept()
            sentence = clientSocket.recv(1024)
            print('client detected! data:',sentence)
            # Processing
            # Todo
            proxy_server(server_ip,8080,clientSocket,addr,sentence)
        except:
            proxySocket.close()
            print('proxy shut down.')
            sys.exit(1)


