# -*- coding: UTF-8 -*-
import time
from config import config_orm_initial

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
User = config_orm_initial.initialize_orm()['dict_user']

# 重设密码
def reset_password(input_email, input_code, input_new_pass):

    # 先看能不能找到这个user，如果找不到就是None
    target_user = session.query(User).filter(User.email == input_email).first()

    # 再看能不能找到匹配的验证码（email，timestamp，purpose，if_used）
    target_code_list = session.query(Mailcode).filter(
        Mailcode.email == input_email,
        Mailcode.purpose == 'reset_password',
        Mailcode.if_used == 0,
        time.time() - Mailcode.timestamp < 1800
    ).all()

    # 如果找到这个user
    try:
        # 如果找到这个user
        # 如果找到匹配的验证码
            # 输入的验证码和找到的验证码是否相等，如果相等
                # 重新设置target_user的密码
            # 如果不相等
                # 返回验证码输入错误
        # 如果找不到匹配的验证码
            # 返回还没有发放验证码或者验证码过期或者验证码已经被使用过




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
        elif bool(1 - judge_if_notused):
            return 'code used'
        elif bool(1 - judge_if_notoverdue):
            return 'code overdue'
        else:
            return 'code error'
    elif bool(1 - inner_user_exist):
        return 'email not exists'
    else:
        