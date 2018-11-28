# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:33:43 2018

@author: zhangwx
"""

from socket import *
HOST = 'localhost'
PORT = 2018
BUFSIZ = 1024
ADDR = (HOST, PORT)
 
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
 
while True:
    data = input('> ')
    if not data:
        continue
    tcpCliSock.send(bytes(data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    print (data.decode('utf-8'))
 

