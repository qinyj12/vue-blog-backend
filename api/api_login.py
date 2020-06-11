# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import request, make_response, session
from orm import orm_login

@app.route('/login', methods = ['GET','POST'])
def login():
	resp = make_response()

	if request.method == 'GET':
		global emal, password
		email = request.args.get('email')
		password = request.args.get('password')

	elif request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

	else:
		resp.data = 'UNKNOWN METHOD'
		return resp

	resp.data = orm_login.login(email, password)
	# session.permanent = True
	# session['username'] = email
	return resp