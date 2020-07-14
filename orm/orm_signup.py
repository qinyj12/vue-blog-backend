# -*- coding: UTF-8 -*-
from sqlalchemy import exists
from flask import current_app

# 从config/orm_initial引入
from config import config_orm_initial
orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
Mailcode = orm['dict_mailcode']
User = orm['dict_user']

#注册
def sign_up(parameter_name, parameter_email, parameter_password, parameter_code):
    # 先拿到当前时间戳
    import time, datetime
    temp_timestamp = round(time.time())
    format_timestamp = datetime.datetime.fromtimestamp(temp_timestamp)

    # 再拿到邮箱验证码的有效期
    temp_validity = current_app.mailcode_validity

    # 先看邮箱有没有被注册过
    if_email_exist = session.query(exists().where(User.email == parameter_email)).scalar()

    # 如果已经被注册过了
    if if_email_exist:
        session.close()
        return {'status': 400, 'result': '邮箱已注册'}

    # 如果还没有被注册过
    else:
        # 核实用户输入的验证码和mailcode表里的是否相等
        target_code_list = session.query(Mailcode).filter(
            Mailcode.email == parameter_email,
            Mailcode.purpose == 'signup',
            temp_timestamp - Mailcode.timestamp < temp_validity,
            Mailcode.if_used == 0,
            Mailcode.code == parameter_code
        ).all()

        # 核实用户输入的验证码和mailcode表里的是否相等——如果能找到相等的，也就是结果不为[]
        if target_code_list:
            # 注册用户到user表
            session.add(
                User(
                    nickname = parameter_name,
                    email = parameter_email, 
                    password = parameter_password, 
                    timestamp = temp_timestamp, 
                    format_updated_time = format_timestamp
                )
            )

            # 找到target_code_list中最新的一个（因为有可能有多个），标记为已使用
            target_code_list[-1].if_used = 1

            # 尝试commit数据库
            try:
                session.commit()
                session.close()
                return {'status': 200, 'result': '注册成功'}

            # 如果发生未知的错误
            except Exception as e:
                current_app.logger.info(str(e))
                session.rollback()
                session.close()
                return {'status': 500, 'result': '服务器出错了'}

        # 核实用户输入的验证码和mailcode表里的是否相等——如果找不到相等的，即结果为[]
        else:
            session.close()
            return {'status': 400, 'result': '验证码错误'}