# -*- coding: UTF-8 -*-
from sqlalchemy import exists
from config import config_orm_initial

# 从config/config_orm_initial引入orm配置
session = config_orm_initial.initialize_orm()['dict_session']
User = config_orm_initial.initialize_orm()['dict_user']

#定义登录方法
def login(parameter_email, parameter_password):
    # 尝试找到password、email相等的记录
    try:
        temp_target = session.query(User).filter(
            User.email == parameter_email,
            User.password == parameter_password
        ).first()

        # 如果没有相等的记录，则为None，那样temp_target.email也是错误的，会跳转except
        session.close()
        return {'status': 200, 
                'result': {'user_email': temp_target.email, 'user_id': temp_target.id}
                }

    # 如果没有找到接收的email、password参数的记录
    except Exception as e:
        session.close()
        return {'status': 400, 'result': '用户名或密码错误'}