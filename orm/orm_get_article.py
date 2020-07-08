# -*- coding: UTF-8 -*-
from flask import current_app

# 从config/config_orm_initial引入orm配置
from config import config_orm_initial
orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
Articlelist = orm['dict_Articlelist']

def get_article(articles_range):
    try:
        # 倒序排序，然后再切片
        temp_target = session.query(Articlelist).order_by(Articlelist.id.desc())[articles_range[0] : articles_range[1]]
        # 获取articlelist表的总条数
        temp_count = session.query(Articlelist).count()

        # 先定义一个list
        temp_list = []
        for i in temp_target:
            temp_list.append(
                {'id':i.id, 'title':i.title, 'abstract':i.abstract, 'avatar':i.avatar, 'time':i.time, 'cover':i.cover, 'views':i.views, 'comments':i.comments}
            )
        session.close()
        return {'status': 200, 'result': {'count': temp_count, 'articleList': temp_list}}

    # 如果发生未知的错误
    except Exception as e:
        current_app.logger.info(e)
        session.close()
        return {'status': 500, 'result': '服务器出错了'}
