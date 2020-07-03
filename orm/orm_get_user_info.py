# -*- coding: UTF-8 -*-
from flask import current_app

# 从config/config_orm_initial引入orm配置
from config import config_orm_initial
session = config_orm_initial.initialize_orm()['dict_session']
user = config_orm_initial.initialize_orm()['dict_user']

def get_user_info(parameter_user_id):
    # try:
        # 根据user_id找到user
    target_user = session.query(user).filter_by(id = parameter_user_id).first()

    import sys
    print(target_user, file=sys.stderr)

    session.close()
        # resp = {
        #     'status': 200, 
        #     'result': {
        #         'id': target_article.nickname,
        #         'email': target_article.email,
        #         'avatar': target_article.avatar
        #     }
        # }
        # return resp

    # 如果发生未知的错误
    # except Exception as e:
    #     current_app.logger.info(e)
    #     session.close()
    #     return {'status': 500, 'result': '服务器出错了'}