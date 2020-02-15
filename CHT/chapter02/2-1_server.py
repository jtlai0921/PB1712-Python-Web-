#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   							#socket模組
import datetime

HOST='0.0.0.0'
PORT=3434

#AF_INET說明使用IPv4位址， SOCK_STREAM指明TCP協定
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
s.bind((HOST,PORT))   						#綁定IP與通訊埠
s.listen(1)         							#監聽

while True:
       conn,addr=s.accept()   				#接收TCP連線，並傳回新的socket
       print'Client %s connected!' % str(addr)    	#輸出用戶端的IP位址
       dt = datetime.datetime.now()
       message = "Current time is " + str(dt)
       conn.send(message)      				#給用戶端傳送目前時間
       print "Sent: ", message
       conn.close()     						#關閉連線
