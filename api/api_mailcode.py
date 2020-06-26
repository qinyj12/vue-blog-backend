# -*- coding: UTF-8 -*-
from flask import request, render_template, jsonify, Blueprint, current_app
from flask_mail import Mail, Message
import re

# 引入外部模块定义的模板文件夹
from config import config_mailcode
app = Blueprint('api_mailcode', __name__, template_folder = config_mailcode.Config().template_folder)

@app.route('/mailcode', methods = ['GET','POST'])
def send_mail():
    # 接收邮箱，和目的
    if request.method == 'GET':
        user_mail = request.args.get('email')
        user_purpose = request.args.get('purpose')
    elif request.method == 'POST':
        user_mail = request.form.get('email')
        user_purpose = request.form.get('purpose')
    # 因为不允许其他方法，所以直接pass
    else:
        pass

    # 配置mail
    from config import config_mail
    current_app.config.from_object(config_mail.Config())
    mail = Mail(current_app)
    msg = Message('hello world', sender='1562555013@qq.com', recipients=[user_mail])
    
    # 引入外部模块，存储验证码到数据库
    from orm import orm_code
    temp_result = orm_code.save_mail_code(user_mail, user_purpose)

    import sys
    print('1', file=sys.stderr)

    # 如果接口返回的状态正常
    if temp_result['status'] == 200:
        print('2', file=sys.stderr)
        # 发邮件
        msg.html = render_template('temp_email.html', name = re.split(r'@', user_mail)[0], code = temp_result['result']) # 提取user_mail中@之前的部分
        print('3', file=sys.stderr)
        try:
            mail.send(msg)
            resp = {
                'status': 200,
                'result': '已发送至 %s' % user_mail
            }
            return jsonify(resp)

        # 有可能邮箱配置会出现问题
        except Exception as e:
            current_app.logger.info(e)
            resp = {
                'status': 500,
                'result': '服务器出错了'
            }
            return jsonify(resp)

    # 如果接口返回的状态异常
    else:
        return jsonify(temp_result)