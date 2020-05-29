# -*- coding: UTF-8 -*-
# 从config/config_orm_initial引入
from config import config_orm_initial
session = config_orm_initial.initialize_orm()['dict_session']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']
User = config_orm_initial.initialize_orm()['dict_user']

# 保存邮件验证码到数据库
def save_mail_code(func_inner_email):

    # 生成随机码
    import random
    list_num = ([random.randint(0,9) for _ in range(4)]) # 4位随机数组成list
    list_str = list(map(lambda x : str(x), list_num)) # 随机数转字符串
    func_inner_code = ''.join(list_str) # 组合字符串

    # 当前时间戳
    import time
    import datetime
    now_time = round(time.time()) # 四舍五入取整
    format_now_time = datetime.datetime.fromtimestamp(now_time)

    # 查看这个email是否存在
    from sqlalchemy import exists
    func_inner_exist = session.query(exists().where(Mailcode.email == func_inner_email)).scalar()
    # 如果email已存在
    if func_inner_exist:
        # 找到最新的email_code记录
        latest_code = session.query(Mailcode).filter(Mailcode.email == func_inner_email).all()[-1]
        # 最新记录的时间戳
        latest_code_time = latest_code.timestamp
        # 判断时间差是否 > 60s
        if now_time - latest_code_time > 60:
            session.add(Mailcode(email = func_inner_email,
                                 code = func_inner_code,
                                 timestamp = now_time,
                                 format_time = format_now_time))
            try:
                session.commit()
                session.close()
                return func_inner_code
            except Exception as e:
                session.rollback()
                session.close()
                return str(e)
        # 判断时间差是否 < 60s
        else:
            return '一分钟内只能发一次哦'

    # 如果之前不存在email_code记录，直接保存
    else:
        session.add(Mailcode(email = func_inner_email,
                             code = func_inner_code,
                             timestamp = now_time,
                             format_time = format_now_time))
        try:
            session.commit()
            session.close()
            return func_inner_code
        except Exception as e:
            session.rollback()
            session.close()
            return str(e)