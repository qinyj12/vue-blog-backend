# -*- coding: UTF-8 -*-
from config import config_orm_initial
from sqlalchemy import exists

# 从config/orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']
User = config_orm_initial.initialize_orm()['dict_user']

#注册
def sign_up(func_inner_name, func_inner_email, func_inner_password, func_inner_code):
    # 先看邮箱有没有被注册过
    inner_email_exist = session.query(exists().where(User.email == func_inner_email)).scalar()

    # 如果已经被注册过了
    if inner_email_exist:
        session.close()
        return 'email has benn signed'
    
    # 如果还没有被注册过
    else:
        # 找到验证码
        target_code_list = session.query(Mailcode).filter(
            Mailcode.email == func_inner_email,
            Mailcode.purpose == 'signup',#还得检查一下别的有没有用过signup
            Mailcode.code == func_inner_code,
        ).all()




    # 看看验证码表有没有这个email
    from sqlalchemy import exists
    func_inner_exist = session.query(exists().where(Mailcode.email == func_inner_email)).scalar()
    if func_inner_exist:
        target_code = session.query(Mailcode).filter(Mailcode.email == func_inner_email).all()[-1]
        # 获取当前时间戳和时间差
        import time
        func_inner_timestamp = round(time.time())
        time_difference = func_inner_timestamp - target_code.timestamp
        # 验证用户输入的code是否正确，并且code还没有被使用过
        if target_code.code == func_inner_code and target_code.if_used == 0 and time_difference < 1800:
            # 格式化时间戳
            import datetime
            func_inner_format_time = datetime.datetime.fromtimestamp(func_inner_timestamp)
            session.add(User(nickname = func_inner_name,
                             email = func_inner_email, 
                             password = func_inner_password, 
                             timestamp = func_inner_timestamp, 
                             format_updated_time = func_inner_format_time))
            try:
                target_code.if_used = 1
                session.commit()
                session.close()
                return 'hello world!'
            except Exception as e:
                session.rollback()
                session.close()
                return str(e)
        # 如果验证码不正确
        elif target_code.code != func_inner_code:
            return 'code error'
            session.close()
        # 如果验证码正确，但是被使用过了
        elif target_code.if_used != 0:
            return 'code used'
            session.close()
        # 如果验证码正确，而且也没被使用过，但是超期了
        elif time_difference >= 1800:
            return 'code overdue : %s' % str(time_difference)

    # 如果验证码表不存在这个email
    else:
        return 'email not found'
        session.close()