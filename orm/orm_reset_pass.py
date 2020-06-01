# -*- coding: UTF-8 -*-
import time
from config import config_orm_initial

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
User = config_orm_initial.initialize_orm()['dict_user']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']
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
    if target_user:
        # 尝试找到匹配的验证码的最后一个
        try:
            target_code = target_code_list[-1]
            # 输入的验证码和找到的验证码是否相等，如果相等
            if target_code.code == input_code:
                # 重新设置target_user的密码
                try:
                    target_user.password = input_new_pass
                    target_code.if_used = 1
                    session.commit()
                    session.close()
                    return 'reset success'
                except Exception as e:
                    session.rollback()
                    session.close()
                    return str(e)
            # 如果不相等
            else:
                return 'code error '
        # 如果找不到匹配的验证码
        except Exception as e:
            return str(e) + ' -- code not find'
    else:
        return 'email not found'