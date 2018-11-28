# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:07:19 2018

@author: zhangwx
"""
from socket import *
HOST = 'www.douyu.com'
PORT = 80
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
tcpCliSock.send(b"GET/\n")
data = tcpCliSock.recv(BUFSIZE)

with open(r"a.txt",'w') as f:
    f.write(data.decode())