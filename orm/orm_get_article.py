# -*- coding: UTF-8 -*-

# 从config/config_orm_initial引入orm配置
session = config_orm_initial.initialize_orm()['dict_session']
Articlelist = config_orm_initial.initialize_orm()['dict_Articlelist']

def get_article(articles_range):
    try:
        temp_target = session.query(Articlelist).filter(
            
        ).first()