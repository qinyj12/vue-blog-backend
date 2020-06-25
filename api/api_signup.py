# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify, current_app

app = Blueprint('api_signup', __name__)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        parameter_nickname = request.args.get('nickname')
        parameter_email = request.args.get('email')
        parameter_password = request.args.get('password')
        parameter_mailcode = request.args.get('mailcode')
    elif request.method == 'POST':
        parameter_nickname = request.form.get('nickname')
        parameter_email = request.form.get('email')
        parameter_password = request.form.get('password')
        parameter_mailcode = request.form.get('mailcode')
    # 本来就不允许其他方法，所以直接pass也没关系
    else:
        pass

    from orm import orm_signup
    temp_result = orm_signup.sign_up(parameter_nickname, parameter_email, parameter_password, parameter_mailcode)

    # 如果接口返回的状态码正常
    if temp_result['status'] == 200:
        return jsonify(temp_result)

    # 如果接口返回的状态码异常
    else:
        current_app.logger.info(temp_result['result'])
        return jsonify(temp_result)