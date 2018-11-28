# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:36:31 2018

@author: zhangwx
"""

import socket
HOST = ''
PORT = 2018
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSocket.bind(ADDR)
tcpSocket.listen(5)

while True:
    print ("等待连接")
    conn,addr = tcpSocket.accept()
    print("从"+addr[0]+"连接")
    while True:
        data = conn.recv(BUFSIZE)
        if data == b'Q':
            conn.close()
        else:
            print("%s:%s"%(addr[0],data.decode('utf-8')))
        senddata = ""
        while senddata == "":
            senddata = input('> ')
        conn.send(bytes(senddata,'utf-8'))
        data = None
conn.close()