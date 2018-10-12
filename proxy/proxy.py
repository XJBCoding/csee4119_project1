#!/usr/bin/env python
from socket import socket, AF_INET, SOCK_STREAM
import time


#import sys

if __name__ == '__main__':
    #print(sys.argv)
    #listen_port = sys.argv[1]
    #fake_ip = sys.argv[2]
    #server_ip = sys.argv[3]
    listen_port = "8080"
    fake_ip = "127.0.0.1"
    server_ip = "127.0.0.1"
    proxySocket = socket(AF_INET, SOCK_STREAM)
    proxySocket.bind(('', int(listen_port)))
    proxySocket.listen(1)
    print('The proxy is ready to receive')
    while True:
        try:
            clientSocket, addr = proxySocket.accept()
            sentence = clientSocket.recv(1024)
            # Processing
            # Todo
            print("receive from: " + str(addr) + " with message: " + sentence)
        except:
            clientSocket.close()
            proxySocket.close()
        try:
            serverSocket = socket(AF_INET, SOCK_STREAM)
            serverSocket.bind((server_ip, 8080))
            serverSocket.send(sentence)
            print("send to" + str(addr) + " with message: " + sentence)
        except:
            serverSocket.close()
            proxySocket.close()


