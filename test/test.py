import glob
a = glob.glob('../static/articles/1/1_*.html')
if a:
    print('123')
else:
    print('456')

# import sys
# sys.path.append('../')
# from config import config_test_orm

# run_orm = config_test_orm.initialize_orm()

# session = run_orm['dict_session']
# user = run_orm['dict_user']
# comment = run_orm['dict_comments']
# article = run_orm['dict_Articlelist']

# target_article = session.query(article).filter(article.id == 1).first()
# # comments_in_range = target_article.relate_comments[0:3]
# # a = list(map(
# #     lambda x:{
# #         'content':x.content, 
# #         'time':x.time, 
# #         'user_name':session.query(user).filter_by(id=x.user_id).one().nickname,
# #         'user_avatar':session.query(user).filter_by(id=x.user_id).one().avatar
# #     }, 
# #     comments_in_range)
# # )
# # print(a)
# comments_list = target_article.relate_comments
# count = [0,2]
# print(comments_list[-1-count[0] : -1-count[1]:-1])
# session.close()




# 尝试给下一篇博客分配id
# import sys
# sys.path.append('../')
# from sqlalchemy import or_
# from sqlalchemy.sql import exists
# from config import config_test_orm

# run_orm = config_test_orm.initialize_orm()

# session = run_orm['dict_session']
# user = run_orm['dict_user']
# comment = run_orm['dict_comments']
# article = run_orm['dict_Articlelist']

# undone_article = session.query(article).filter(or_(article.if_done != 1, article.if_done == None))
# done_article = session.query(article).filter_by(if_done = 1)
# all_article = session.query(article)

# undone_count = undone_article.count()
# all_count = all_article.count()
# done_count = done_article.count()

# target = undone_article.one()
# session.delete(target)
# session.commit()
# session.close()
