# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import request, make_response
from orm import orm_login

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    # return(orm_login.login(email, password))

    resp = make_response()
    resp.headers['Access-Control-Allow-Credentials'] = true
    resp.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    # resp.data = orm_login.login(email, password)
    resp.data = 'yes'
    return resp