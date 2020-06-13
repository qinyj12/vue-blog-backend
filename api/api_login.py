# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import request, make_response, session, abort
from orm import orm_login

# https://www.cnblogs.com/cwp-bg/p/8946394.html

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

	temp_result = orm_login.login(email, password)

	# 查看接口返回值的status状态
	if temp_result['status'] == 200:

		# 给用户的session中插入user_name和user_id
		session['user_email'] = temp_result['result']['user_email']
		session['user_id'] = temp_result['result']['user_id']

		resp.data = temp_result['result']['user_email']
		app.logger.info('%s logged in successfully' % temp_result['result']['user_email'])
		return resp

	else:
		abort(404)