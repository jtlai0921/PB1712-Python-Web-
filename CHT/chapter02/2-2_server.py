#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   						#socket模組

HOST='0.0.0.0'
PORT=3434

#AF_INET說明使用IPv4位址， SOCK_ DGRAM指明UDP協定
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
s.bind((HOST,PORT))   					#綁定IP與通訊埠

while True:
    data, addr = s.recvfrom(1024)			#本次接收最大資料長度1024
    print "Received: %s from %s" % (data, str(addr))

s.close()
