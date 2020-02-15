#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, session
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'SET_ME_BEFORE_USE_SESSION'

@app.route('/write_session')
def writeSession():
    session['key_time']= datetime.now().strftime('%Y-%m-%d %H:%M:%S')		#將目前時間儲存在Session中	
    return session['key_time']  			#傳回目前時間
 
@app.route('/read_session')
def readSession():
    return session.get('key_time')			#獲得上次呼叫writeSession時寫入的時間，並傳回

if __name__ == '__main__':
    app.run()
