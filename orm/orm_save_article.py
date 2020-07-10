# -*- coding: UTF-8 -*-
from config import config_orm_initial
from flask import current_app, abort
from orm import orm_get_next_article_id

# 从config/config_orm_initial引入
orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
Article_list = orm['dict_Articlelist']

def save_article(parameter_title, parameter_abstract, parameter_avatar, parameter_cover, parameter_time):
    # 从orm/orm_get_next_article_id引入
    current_article_id = orm_get_next_article_id.return_next_article_id()
    temp_status = current_article_id['status']
    temp_id = current_article_id['result']

    # 如果current_article_id返回的status是201，代表是改记录而不是增记录，直接把这条记录删除，然后重新新增
    if temp_status == 201:
        target_record = session.query(Article_list).filter_by(id = temp_id).one()
        try:
            # 删除记录
            session.delete(target_record)
            # 新增记录
            new_article = Article_list(
                id = temp_id,
                title = parameter_title,
                abstract = parameter_abstract,
                avatar = parameter_avatar,
                cover = parameter_cover,
                time = parameter_time,
                views = 0,
                comments = 0,
                if_done = 1
            )
            session.add(new_article)
            session.commit()
            session.close()
            return {'status': 200, 'result': temp_id}
        except Exception as e:
            current_app.logger.info(e)
            session.rollback()
            session.close()
            abort(500)

    # 如果next_id返回的status是200，就代表要新增一条记录
    else:
        new_article = Article_list(
            id = temp_id,
            title = parameter_title,
            abstract = parameter_abstract,
            avatar = parameter_avatar,
            cover = parameter_cover,
            time = parameter_time,
            views = 0,
            comments = 0,
            if_done = 1
        )
        try:
            session.add(new_article)
            session.commit()
            session.close()
            return {'status': 200, 'result': temp_id}
        except Exception as e:
            current_app.logger.info(e)
            session.rollback()
            session.close()
            abort(500)