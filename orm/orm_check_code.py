# -*- coding: UTF-8 -*-
from sqlalchemy import exists
from config import config_orm_initial
from flask import current_app

# 从config/config_orm_initial引入orm配置
session = config_orm_initial.initialize_orm()['dict_session']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']

# 定义核对邮件验证码的方法
def check_code(parameter_email, parameter_code, parameter_purpose):
    # 拿到邮件验证码的有效期（300s）
    temp_code_validity = current_app.mailcode_validity

    # 拿到当前时间戳
    import time
    temp_timestamp = time.time()

    # 尝试找到email、code、purpose相等的记录，还得在有效期内，还得没有使用过
    try:
        # all()或first()如果没有找到的话分别是None和[]，如果再试图通过[-1]来找到最后一个值就会出错
        temp_target = session.query(Mailcode).filter(
            Mailcode.email == parameter_email,
            Mailcode.code == parameter_code,
            Mailcode.purpose == parameter_purpose,
            temp_timestamp - Mailcode.timestamp < temp_code_validity,
            Mailcode.if_used == 0
        ).all()[-1]

        # 定义status状态，以给接口捕获状态
        session.close()
        return {'status': 200, 
                'result': '验证通过'
                }

    # 如果没有找到接收的email、password参数的记录，也就是temp_target的结果为[]
    except Exception as e:
        session.close()
        return {'status': 400, 'result': '验证未通过'}


