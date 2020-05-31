# -*- coding: UTF-8 -*-
import random
import time
import datetime
from sqlalchemy.sql import exists, and_
from config import config_orm_initial

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']
User = config_orm_initial.initialize_orm()['dict_user']

# 保存邮件验证码到数据库
def save_mail_code(func_inner_email, func_inner_purpose):

    # 生成随机码
    list_num = ([random.randint(0,9) for _ in range(4)]) # 4位随机数组成list
    list_str = list(map(lambda x : str(x), list_num)) # 随机数转字符串
    func_inner_code = ''.join(list_str) # 组合字符串

    # 当前时间戳
    now_time = round(time.time()) # 四舍五入取整
    format_now_time = datetime.datetime.fromtimestamp(now_time)

    # 定义一个方法，保存到数据库
    def inner_save_code():
        session.add(
            Mailcode(
                email = func_inner_email,
                code = func_inner_code,
                timestamp = now_time,
                format_time = format_now_time,
                purpose = func_inner_purpose
            )
        )
        try:
            session.commit()
            session.close()
            return func_inner_code
        except Exception as e:
            session.rollback()
            session.close()
            return str(e)

    # 如果表里没有邮箱的记录，直接保存
    if bool(1 - session.query(exists().where(Mailcode.email == func_inner_email)).scalar()):
        # 调用临时定义的保存数据库的方法
        return inner_save_code()

    # 如果表里已有这个邮箱的记录，多重判断
    else:
        # 这个邮箱是否在60秒内发过同一purpose的验证码
        if_too_often = session.query(exists().where(
            and_(
                Mailcode.email == func_inner_email,
                Mailcode.purpose == func_inner_purpose,
                Mailcode.if_used == 0,
                now_time - Mailcode.timestamp < 60
            )
        )).scalar()

        # 如果这个邮箱60s内已经发过验证码了
        if if_too_often:
            return 'too often'

        # 60s内没有发过验证码，或者没有找到purpose==func_inner_purpose的验证码
        else:
            return inner_save_code()