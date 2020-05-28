# -*- coding: UTF-8 -*-
# 从config/orm_initial引入
from config import orm_initial
session = orm_initial.initialize_orm()['dict_session']
Mailcode = orm_initial.initialize_orm()['dict_mailcode']
User = orm_initial.initialize_orm()['dict_user']

#注册
def sign_up(func_inner_name, func_inner_email, func_inner_password, func_inner_code):
    # 尝试在验证码表里找这个email，就是排在最后一个的
    try:
        target = session.query(Mailcode).filter(Mailcode.email == func_inner_email).all()[-1]
        # 验证用户输入的code是否正确，并且code还没有被使用过
        if target.code == func_inner_code and target.if_used == 0:
            # 获取当前时间戳
            import time
            func_inner_timestamp = round(time.time())
            # 判断时间戳是否过期
            if func_inner_timestamp - target.timestamp < 1800:
                # 格式化时间戳
                import datetime
                func_inner_format_time = datetime.datetime.fromtimestamp(func_inner_timestamp)
                session.add(User(nickname = func_inner_name,
                                 email = func_inner_email, 
                                 password = func_inner_password, 
                                 timestamp = func_inner_timestamp, 
                                 format_updated_time = func_inner_format_time))
                try:
                    target.if_used = 1
                    session.commit()
                    session.close()
                    return 'hello world!'
                except Exception as e:
                    session.rollback()
                    session.close()
                    return str(e)
            else:
                # 超期了
                return 'code overdue : %s' % str(func_inner_timestamp - target.timestamp)
        # 如果验证码不正确
        elif target.code != func_inner_code:
            return 'code error'
            session.close()
        elif target.if_used != 0:
            return 'code used'
            session.close()
    # 如果验证码表不存在这个email
    except:
        return 'email not found'
        session.close()