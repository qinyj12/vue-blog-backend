# -*- coding: UTF-8 -*-
from config import config_orm_initial
from sqlalchemy import exists
import time
import datetime

# 从config/orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']
User = config_orm_initial.initialize_orm()['dict_user']

#注册
def sign_up(func_inner_name, func_inner_email, func_inner_password, func_inner_code):
    # 先拿到当前时间戳
    inner_timestamp = round(time.time())
    format_inner_timestamp = datetime.datetime.fromtimestamp(inner_timestamp)

    # 先看邮箱有没有被注册过
    inner_email_exist = session.query(exists().where(User.email == func_inner_email)).scalar()

    # 如果已经被注册过了
    if inner_email_exist:
        session.close()
        return 'email has been signed'
    
    # 如果还没有被注册过
    else:
        # 找到验证码
        target_code_list = session.query(Mailcode).filter(
            Mailcode.email == func_inner_email,
            Mailcode.purpose == 'signup',
            time.time() - Mailcode.timestamp < 1800,
            Mailcode.if_used == 0,
            Mailcode.code == func_inner_code
        ).all()
        # 如果能找到
        if target_code_list:
            session.add(
                User(
                    nickname = func_inner_name,
                    email = func_inner_email, 
                    password = func_inner_password, 
                    timestamp = inner_timestamp, 
                    format_updated_time = format_inner_timestamp
                )
            )
            # 找到target_code_list中最新的一个
            target_code_list[-1].if_used = 1
            try:
                session.commit()
                session.close()
                return 'hello world!'
            except Exception as e:
                session.rollback()
                session.close()
                return str(e)
        # 如果找不到
        else:
            session.close()
            return 'code not found'