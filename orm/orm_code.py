# -*- coding: UTF-8 -*-
# 从config/orm_initial引入
from config import orm_initial
session = orm_initial.initialize_orm()['dict_session']
Mailcode = orm_initial.initialize_orm()['dict_mailcode']
User = orm_initial.initialize_orm()['dict_user']

# 保存邮件验证码到数据库
def save_mail_code(func_inner_email, func_inner_code):
    # 找到这个email最新的记录
    latest = session.query(Mailcode).filter(Mailcode.email == func_inner_email).all()[-1]
    # 如果存在
    if latest:
        # 最新记录的时间戳
        latest_time = latest.timestamp
        # 当前时间戳
        import time
        import datetime
        now_time = time.time()
        format_now_time = datetime.datetime.fromtimestamp(now_time)
        # 判断时间差是否 > 60s
        if now_time - latest_time > 60:
            session.add(Mailcode(email = func_inner_email,
                                 code = func_inner_code,
                                 timestamp = now_time,
                                 format_time = format_now_time))
            try:
                session.commit()
                session.close()
                return 'codeSaved'
            except Exception as e:
                session.rollback()
                session.close()
                return str(e)
        # 如果 < 60s
        else:
            return '一分钟内只能发一次哦'
    # 如果不存在latest记录，直接保存
    else:
        # 当前时间戳
        import time
        import datetime
        now_time = time.time()
        format_now_time = datetime.datetime.fromtimestamp(now_time)
        session.add(Mailcode(email = func_inner_email,
                             code = func_inner_code,
                             timestamp = now_time,
                             format_time = format_now_time))
        try:
            session.commit()
            session.close()
            return 'codeSaved'
        except Exception as e:
            session.rollback()
            session.close()
            return str(e)