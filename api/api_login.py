# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import request, make_response
from orm import orm_login

@app.route('/login', methods = ['GET','POST'])
def login():

	if request.method == 'GET':
		global emal, password
		email = request.args.get('email')
		password = request.args.get('password')

	elif request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

	resp = make_response()
	resp.headers['AAAA'] = email
	resp.headers['AABB'] = password

	resp.data = orm_login.login(email, password)
	return resp