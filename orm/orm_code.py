# -*- coding: UTF-8 -*-
import random, time, datetime
from sqlalchemy.sql import exists, and_
from config import config_orm_initial
from flask import current_app


# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']
User = config_orm_initial.initialize_orm()['dict_user']

# 保存邮件验证码到数据库
def save_mail_code(parameter_email, parameter_purpose):

    # 生成随机码
    list_num = ([random.randint(0,9) for _ in range(4)]) # 4位随机数组成list
    list_str = list(map(lambda x : str(x), list_num)) # 随机数转字符串
    four_random_numbers = ''.join(list_str) # 组合字符串

    # 当前时间戳
    now_time = round(time.time()) # 四舍五入取整
    format_now_time = datetime.datetime.fromtimestamp(now_time)

    # 定义一个方法，保存到数据库
    def inner_save_code():
        session.add(
            Mailcode(
                email = parameter_email,
                code = four_random_numbers,
                timestamp = now_time,
                format_time = format_now_time,
                purpose = parameter_purpose
            )
        )
        # 尝试保存到数据库
        try:
            session.commit()
            session.close()
            return {'status': 200, 'result': four_random_numbers}
        # 如果发生未知的错误
        except Exception as e:
            session.rollback()
            session.close()
            current_app.logger.info(e)
            return {'status': 500, 'result': str(e)}

    # 如果表里没有邮箱的记录，直接保存
    if bool(1 - session.query(exists().where(Mailcode.email == parameter_email)).scalar()):
        # 调用刚才定义的保存到数据库的方法
        return inner_save_code()

    # 如果表里已有这个邮箱的记录，多重判断
    else:
        # 这个邮箱是否在60秒内发过同一purpose的验证码
        if_too_often = session.query(exists().where(
            and_(
                Mailcode.email == parameter_email,
                Mailcode.purpose == parameter_purpose,
                Mailcode.if_used == 0,
                now_time - Mailcode.timestamp < current_app.mailcode_too_often
            )
        )).scalar()

        # 如果这个邮箱60s内已经发过验证码了
        if if_too_often:
            session.close()
            return {'status': 400, 'result': '太频繁啦'}

        # 60s内没有发过验证码，或者没有找到purpose==parameter_purpose的验证码
        else:
            session.close()
            return inner_save_code()