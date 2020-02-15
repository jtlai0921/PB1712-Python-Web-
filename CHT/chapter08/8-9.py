#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def f_root():
    pass

@app.route('/industry')
def f_industry():   pass

@app.route('/book/<book_name>')
def f_book(book_name):  pass

with app.test_request_context():
    print url_for('f_root')							#例1，輸出：/
    print url_for('f_industry')						#例2，輸出：/industry
    print url_for('f_industry', name='web')				#例3，輸出：/industry?name=web
    print url_for('f_book', book_name='Python Book')	#例4，輸出：/book/Python%20Book
