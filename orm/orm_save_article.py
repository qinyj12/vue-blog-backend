# -*- coding: UTF-8 -*-
from config import config_orm_initial
from flask import current_app as app

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Article_list = config_orm_initial.initialize_orm()['dict_Articlelist']

# 保存正文id（自增主键）、标题、摘要、头像名、时间到数据库
def save_article(inner_title, inner_abstract, inner_avatar, inner_time):
    try:
        session.add(
            Article_list(
                title = inner_title,
                abstract = inner_abstract,
                avatar = inner_avatar,
                time = inner_time
            )
        )

    except Exception as e:
        app.logger.info(e)

    try:
        session.commit()
        session.close()
        return inner_title

    except Exception as e:
        session.rollback()
        session.close()
        app.logger.info(e)