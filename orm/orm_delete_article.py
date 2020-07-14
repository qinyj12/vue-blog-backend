# -*- coding: UTF-8 -*-
from config import config_orm_initial
from flask import current_app

# 从config/config_orm_initial引入
orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
Article_list = orm['dict_Articlelist']


def delete_article(parameter_article_id):
    try:
        # 删除数据库里的记录
        target_article = session.query(Article_list).filter_by(
            id = parameter_article_id
        ).first()
        session.delete(target_article)
        session.commit()
        session.close()

        # 删除这篇article的专属目录
        import shutil
        shutil.rmtree(current_app.article_path + str(parameter_article_id))

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