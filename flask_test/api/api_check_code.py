# -*- coding: UTF-8 -*-
from flask import request, jsonify, Blueprint

app = Blueprint('api_check_code', __name__)

@app.route('/checkcode', methods = ['GET','POST'])
def check_code():
    # 接收邮箱，和目的
    if request.method == 'GET':
        user_mail = request.args.get('email')
        user_code = request.args.get('mailcode')
        user_purpose = request.args.get('purpose')
    elif request.method == 'POST':
        user_mail = request.form.get('email')
        user_code = request.form.get('mailcode')
        user_purpose = request.form.get('purpose')
    # 因为不允许其他方法，所以直接pass
    else:
        pass

    # 引入外部模块，核实邮件验证码
    from orm import orm_check_code
    temp_result = orm_check_code.check_code(user_mail, user_code, user_purpose)

    # 把外部模块的返回值给return出去
    return jsonify(temp_result)