# -*- coding: UTF-8 -*-
import time
from config import config_orm_initial

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
User = config_orm_initial.initialize_orm()['dict_user']
Mailcode = config_orm_initial.initialize_orm()['dict_mailcode']
# 重设密码
def reset_password(parameter_email, parameter_code, parameter_pass):

    # 先看能不能找到这个user，如果找不到就是None
    target_user = session.query(User).filter(User.email == parameter_email).first()

    # 再看能不能找到匹配的验证码（email，timestamp，purpose，if_used）
    target_code_list = session.query(Mailcode).filter(
        Mailcode.email == parameter_email,
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
            if target_code.code == parameter_code:
                # 重新设置target_user的密码
                try:
                    target_user.password = parameter_pass
                    target_code.if_used = 1
                    session.commit()
                    session.close()
                    return {'status': 200, 'result': 'reset success'}
                # 如果发生未知错误
                except Exception as e:
                    session.rollback()
                    session.close()
                    return {'status': 500, 'result': str(e)}

            # 如果找到了验证码，但是和用户输入的不匹配
            else:
                return {'status': 400, 'result': 'code error'}

        # 如果没给这个邮箱发过符合要求的验证码
        except Exception as e:
            return {'status': 400, 'result': 'code not found'}

    # 如果找不到user，即根本没给这个邮箱发过任何验证码
    else:
        return {'status': 400, 'result': 'email not found'}