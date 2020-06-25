# -*- coding: UTF-8 -*-
from config import config_orm_initial

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Article_list = config_orm_initial.initialize_orm()['dict_Articlelist']


def save_article(parameter_title, parameter_abstract, parameter_avatar, parameter_time):
    # 保存正文id（自增主键）、标题、摘要、头像名、时间到数据库
    try:
        session.add(
            Article_list(
                title = parameter_title,
                abstract = parameter_abstract,
                avatar = parameter_avatar,
                time = parameter_time
            )
        )
        session.commit()
        session.close()
        return {'status': 200, 'result': 'save success'}

    # 如果发生未知错误
    except Exception as e:
        session.rollback()
        session.close()
        return {'status': 500 , 'result': str(e)}