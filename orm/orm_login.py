# -*- coding: UTF-8 -*-
from sqlalchemy import exists
from config import config_orm_initial
from flask import current_app

# 从config/config_orm_initial引入orm配置
orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
user = orm['dict_user']

#定义登录方法
def login(parameter_email, parameter_password):
    # 尝试找到password、email相等的记录
    temp_target = session.query(user).filter_by(
        email = parameter_email,
        password = parameter_password
    ).scalar()
    # 如果能找到记录
    if temp_target:
        session.close()
        return {'status': 200, 
                'result': {'user_email': temp_target.email, 'user_id': temp_target.id}
                }
    # 如果找不到记录
    else:
        session.rollback()
        session.close()
        return {'status': 400, 'result': '用户名或密码错误'}