# -*- coding: UTF-8 -*-
from sqlalchemy import exists
from config import config_orm_initial

# 从config/config_orm_initial引入orm配置
session = config_orm_initial.initialize_orm()['dict_session']
User = config_orm_initial.initialize_orm()['dict_user']

#定义登录方法
def login(func_inner_email, func_inner_password):
    # 尝试找到password、email相等的记录
    try:
        inner_target = session.query(User).filter(
            User.email == func_inner_email,
            User.password == func_inner_password
        ).first()
        # 定义status状态，以给接口捕获状态
        return {'status': 200, 
                'result': {'user_email': inner_target.email, 'user_id': inner_target.id}
                }

    # 如果没有找到接收的email、password参数的记录
    except Exception as e:
        return {'status': 400, 'result': str(e)}