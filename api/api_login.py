# -*- coding: UTF-8 -*-
from flask import request, session, Blueprint, jsonify
from orm import orm_login

app = Blueprint('api_login', __name__)

@app.route('/login', methods = ['GET','POST'])
def login():
    # 如果是get方法
    if request.method == 'GET':
        global emal, password
        email = request.args.get('email')
        password = request.args.get('password')
    # 如果是post方法
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    # 因为不允许其他方法，所以直接return就完了
    else:
        return

    # 拿到浏览器请求的email和password后，调用orm_login.login接口
    temp_result = orm_login.login(email, password)

    # 查看接口返回值的status状态，如果状态正常
    if temp_result['status'] == 200:
        # 给用户的浏览器session中插入user_name和user_id
        session['user_email'] = temp_result['result']['user_email']
        session['user_id'] = temp_result['result']['user_id']

        return jsonify(temp_result)

    # 如果接口返回的状态不正常,即用户输入email、password不对
    else:
        return jsonify(temp_result)