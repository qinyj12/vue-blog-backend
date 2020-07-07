# -*- coding: UTF-8 -*-
from config import config_orm_initial
from flask import current_app

session = config_orm_initial.initialize_orm()['dict_session']
Articlelist = config_orm_initial.initialize_orm()['dict_Articlelist']
User = config_orm_initial.initialize_orm()['dict_user']

def get_comments(article_id, comments_range):
    try:
        # 尝试拿到这个article，并且调用relationship拿到comments，而且在comments_range的范围里
        target_article = session.query(Articlelist).filter_by(id = article_id).first()
        target_comments = target_article.relate_comments[comments_range[0] : comments_range[1]]

        # 先定义一个list
        temp_list = []
        for i in target_comments:
            temp_list.append({
                'content': i.content, 
                'time': i.time, 
                'user_id': i.user_id, 
                'user_nickname': i.relate_user.nickname, 
                'user_avatar': i.relate_user.avatar
            })

        resp = {'status': 200, 'result': temp_list}
        session.close()
        return resp
    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 200, 'result': '服务器出错了'}
        session.rollback()
        session.close()
        return resp