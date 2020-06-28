# -*- coding: UTF-8 -*-
from config import config_orm_initial
from flask import current_app

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Article_list = config_orm_initial.initialize_orm()['dict_Articlelist']


def save_article(parameter_title, parameter_abstract, parameter_avatar, parameter_cover, parameter_time):
    # 保存正文id（自增主键）、标题、摘要、头像名、时间到数据库
    try:
        new_article = Article_list(
            title = parameter_title,
            abstract = parameter_abstract,
            avatar = parameter_avatar,
            cover = parameter_cover,
            time = parameter_time,
            views = 0,
            comments = 0
        )
        session.add(new_article)
        session.commit()
        # 要先拿到id，然后再close，不然就拿不到了
        article_id = new_article.id
        session.close()
        return {
            'status': 200, 
            'result': {
                'result': '保存成功',
                'article_id': article_id
            }
        }

    # 如果发生未知错误
    except Exception as e:
        session.rollback()
        session.close()
        current_app.logger.info(e)
        return {'status': 500 , 'result': '服务器错误'}