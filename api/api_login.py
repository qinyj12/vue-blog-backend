# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import request

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    from orm import orm_login
    return(orm_login.login(email, password))