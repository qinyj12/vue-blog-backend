# -*- coding: UTF-8 -*-
# 从config/config_orm_initial引入
from config import config_orm_initial
session = config_orm_initial.initialize_orm()['dict_session']
User = config_orm_initial.initialize_orm()['dict_user']

#注册
def login(func_inner_email, func_inner_password):

    # 先看user表里有没有这个email
    from sqlalchemy import exists
    func_inner_exist = session.query(exists().where(User.email == func_inner_email)).scalar()
    # 如果user表里有这个email
    if func_inner_exist:
        # 找到这个email用户
        target_user = session.query(User).filter(User.email == func_inner_email).first()
        if target_user.password == func_inner_password:
            return 'login successed'
        else:
            return 'password incorrect'
    # 如果验证码表里没有这个email
    else:
        return 'email not signed up'