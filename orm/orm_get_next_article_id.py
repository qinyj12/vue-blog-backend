# -*- coding: UTF-8 -*-
from sqlalchemy import or_
from config import config_orm_initial
from flask import current_app, abort

def return_next_article_id():
    run_orm = config_orm_initial.initialize_orm()
    session = run_orm['dict_session']
    user = run_orm['dict_user']
    comment = run_orm['dict_comments']
    article = run_orm['dict_Articlelist']

    undone_article = session.query(article).filter(or_(article.if_done != 1, article.if_done == None))
    done_article = session.query(article).filter_by(if_done = 1)
    undone_count = undone_article.count()
    done_count = done_article.count()

    try:
        if done_count == 0:
            next_id = 1
            # 200代表需要在数据库新增记录，201代表需要改动数据库已有的记录
            return {'status': 200, 'result': next_id}
        elif undone_count == 0:
            next_id = done_article[-1].id + 1
            return {'status': 200, 'result': next_id}
        else:
            next_id = undone_article.first().id
            return {'status': 201, 'result': next_id}
        session.close()
        
    except Exception as e:
        current_app.logger.info(e)
        session.rollback()
        session.close()
        abort(500)
