# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify, current_app

app = Blueprint('api_reset_password', __name__)

@app.route('/resetpass', methods = ['GET','POST'])
def reset_password():
    if request.method == 'GET':
        email = request.args.get('email')
        mailcode = request.args.get('mailcode')
        new_pass = request.args.get('new_pass')
    elif request.method == 'POST':
        email = request.form.get('email')
        mailcode = request.form.get('mailcode')
        new_pass = request.form.get('new_pass')
    # 因为不允许其他方法，所以直接pass也没关系
    else:
        pass

    from orm import orm_reset_pass
    temp_result = orm_reset_pass.reset_password(email, mailcode, new_pass)

    # 如果接口返回的状态码正常
    if temp_result['status'] == 200:
        return jsonify(temp_result)

    # 如果接口返回的状态码异常
    else:
        current_app.logger.info(temp_result['result'])
        return jsonify(temp_result)