#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket   					#socket模組

HOST='127.0.0.1'
PORT=3434

#AF_INET說明使用IPv4位址， SOCK_STREAM指明TCP協定
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   

s.connect((HOST, PORT))
print "Connect %s:%d OK" % (HOST, PORT)
data = s.recv(1024)   				#接收資料，本次接收資料的最大長度為1024
print "Received: ", data
s.close()                   			#關閉連線
