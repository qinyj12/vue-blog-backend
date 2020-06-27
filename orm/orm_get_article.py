# -*- coding: UTF-8 -*-

# 从config/config_orm_initial引入orm配置
session = config_orm_initial.initialize_orm()['dict_session']
Articlelist = config_orm_initial.initialize_orm()['dict_Articlelist']

def get_article(articles_range):
    try:
        articles_range.sort()
        temp_target = session.query(Articlelist).slice(articles_range[0], articles_range[1]).all()