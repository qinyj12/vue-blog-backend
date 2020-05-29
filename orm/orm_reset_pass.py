# -*- coding: UTF-8 -*-
# 从config/config_orm_initial引入
from config import config_orm_initial
session = config_orm_initial.initialize_orm()['dict_session']
User = config_orm_initial.initialize_orm()['dict_user']

# 重设密码
def reset_password(input_email, input_code, input_new_pass):
    # from sqlalchemy import exists
    inner_user_exist = session.query(exists().where(User.email == input_email)).scalar()
    inner_code_exist = session.query(exists().where(Mailcode.email == input_email)).scalar()

    # 如果存在这个user，并且存在这个email的code
    if inner_user_exist and inner_code_exist:
        # 获取当前时间戳
        import time
        inner_now_timestamp = round(time.time())        
        # 找到这个email_code
        target_mail_code = session.query(Mailcode).filter(Mailcode.email == input_email).all()[-1]
        # 判断email_code有没有被使用过，有没有过期，是不是和用户输入的相等
        judge_if_notused = (target_mail_code.if_used == 0)
        judge_if_notoverdue = (inner_now_timestamp - target_mail_code.timestamp < 1800)
        judge_if_equal = (target_mail_code.code == input_code)
        if judge_if_notused and judge_if_notoverdue and judge_if_equal:
            # 找到这个user
            target_user = session.query(User).filter(User.email == input_email).first()
            # 修改这个user的密码
            try:
                target_user.password = input_email
                session.commit()
                session.close()
                return 'reset success'
            except Exception as e:
                session.rollback()
                session.close()
                return str(e)
        elif !judge_if_notused:
            return 'code used'
        elif !judge_if_notoverdue:
            return 'code overdue'
        else:
            return 'code error'
    elif !inner_user_exist:
        return 'email not exists'
    else:
        