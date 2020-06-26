# -*- coding: UTF-8 -*-
from config import config_orm_initial
from flask import current_app

# 从config/config_orm_initial引入
session = config_orm_initial.initialize_orm()['dict_session']
Article_list = config_orm_initial.initialize_orm()['dict_Articlelist']


def delete_article(parameter_article_id):
    try:
        target_article = session.query(Article_list).filter_by(
            id = parameter_article_id
        ).first()

        session.delete(target_article)
        session.commit()
        session.close()
        return {
            'status': 200, 
            'result': '成功删除'
        }

    # 如果发生未知错误
    except Exception as e:
        session.rollback()
        session.close()
        current_app.logger.info(e)
        return {'status': 500 , 'result': '服务器错误'}