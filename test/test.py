# 导入上级目录
# import sys
# sys.path.append('..')
# from config import config_mailcode
# print(config_mailcode.Config().template_folder)

# from test2 import main
# print(main.hello())
# 操作数据库
# import sqlite3
# conn = sqlite3.connect('../database/database.db')
# cursor = conn.cursor()
# cursor.execute('ALTER TABLE mailcode ADD column purpose STRING(20)')
# cursor.execute('ALTER TABLE user RENAME COLUMN name TO nickname')
# cursor.close()
# conn.commit()
# conn.close()
# 获取当前时间
# import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 调用外部接口查找数据库
# import time
# import sys
# sys.path.append('../')
# from config import config_test_orm

# session = config_test_orm.initialize_orm()['dict_session']
# Mailcode = config_test_orm.initialize_orm()['dict_mailcode']
# User = config_test_orm.initialize_orm()['dict_user']
# Articlelist = config_test_orm.initialize_orm()['dict_Articlelist']


# target = session.query(Articlelist)[-2:-1]

# for i in target:
#     print(i.id)
# session.close()

# func_inner_email = 'qinyj12@126.com'

# inner_result = session.query(User).filter(User.email == func_inner_email).first()

# print(inner_result)

# 多条件判断
# email = 'qinyj12@126.com'

# target_code_list = session.query(Mailcode).filter(
#     Mailcode.email == 'qinyj12@126.com',
#     # Mailcode.purpose == 'reset_password',
#     Mailcode.if_used == 0,
#     time.time() - Mailcode.timestamp < 180000
# ).all()

# if target_code_list:
#     print('yes')
# else:
#     print('no')
# 转换时间戳
# import time, datetime
# timeStamp = 1590506090
# dateArray = datetime.datetime.fromtimestamp(timeStamp)
# print(dateArray)
# 四舍五入取整数时间戳
# import time
# print(round(time.time()))
# 异常处理的方法
# try:
#   print('try...')
#   r = 10 / 0
#   print('result:', r)
# except ZeroDivisionError as e:
#   print('except:', e)
# finally:
#   print('finally...')
# 密码强度，总长度>=9，有数字，有英文
# def checkio(s):
#     fs = ''.join(filter(str.isalnum, s)) # keep only letters and digits
#     return (
#             len(fs) >= 1        # There is at least one letter or digit
#         and len(s)  >= 10       # ... and there are at least 10 characters
#         and not fs.isalpha()    # ... and there is at least one digit
#         and not fs.isdigit()    # ... and there is at least one letter
#         and not fs.islower()    # ... and not all letters are lowercase
#         and not fs.isupper()    # ... and not all letters are uppercase
#     )
# def mycheck(s):
#     fs = ''.join(filter(str.isalnum, s)) # keep only letters and digits
#     return (
#             len(fs) >= 1        # There is at least one letter or digit
#             and len(s) >= 9       # ... and there are at least 10 characters
#             and not fs.isalpha()    # ... and there is at least one digit
#             and not fs.isdigit()    # ... and there is at least one letter
#     )
# 测试try
# try:
#     if 1 == 0:
#         c = 'yes'
#     else:
#         c = 'not'
# except Exception as e:
#     c = 'no'
# print(c)

# 测试dict
# a = {'a':'123', 'b':'234'}
# print(a['a'])

# 测试json
# import json

# data = {
#     'no' : 1,
#     'name' : 'Runoob',
#     'url' : 'http://www.runoob.com'
# }
# json_str = json.dumps(data)
# print ("JSON 对象：", json_str)
# data2 = json.loads(json_str)
# print(data2['no'])

# 测试协程
# import asyncio
# async def a():
#     await c()
#     print('a has been finished')
# async def b():
#     await asyncio.sleep(2)
#     print('b has been finished')
# async def c():
#     await asyncio.sleep(2.1)
#     print('now running a customized function')
# loop = asyncio.get_event_loop()
# tasks = [a(), b()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 测试切片
# a=[1,2,3,4]
# print(a[-1:-3:-1])

# 测试数据库切片
# import sys
# sys.path.append('../')
# from config import config_test_orm

# session = config_test_orm.initialize_orm()['dict_session']
# Mailcode = config_test_orm.initialize_orm()['dict_mailcode']
# User = config_test_orm.initialize_orm()['dict_user']
# Articlelist = config_test_orm.initialize_orm()['dict_Articlelist']

# target = session.query(Articlelist).order_by(Articlelist.id.desc())[0:5]

# temp_list = []
# f_2 = lambda x: temp_list.append({'id': x.id, 'title': x.title})
# list(map(f_2, target))
# print(temp_list)

# session_length = session.query(Articlelist).count()

# print(session_length)

# session.close()

# 测试生成数据库
# import sys
# sys.path.append('../')
# from config import config_test_orm

# config_test_orm.initialize_orm()

# 测试获取类型
# a = [0,1]
# # print(isinstance(a, list))
# print(len(a))

# 测试剪切图片(即移动文件)
# import shutil, os.path
# path = '../static/images/temp/'
# a = 'dog.jpg'
# print(os.path.isfile('../static/images/temp/' + a))
# shutil.move('../static/images/temp/dog.jpg','../static/images/covers/[1]dog.jpg')

# 测试删除文件
# import re, os

# a = "[1]fir.md"

# b = re.match(r'\[(\d+)\](.*)',a)

# print(b.group(2))

# os.remove('../static/articles/[1]1.md')

# 测试读取md文件
# import glob
# article_id = '2'
# file_names = glob.glob('../static/articles/' + '[[]' + article_id + '[]]' + '*.md')[0]

# with open(file_names) as f:
#     print(f.read())

# 测试生成文件
# file_name = '../static/articles/test.txt'

# with open(file_name, 'w'):
#     pass

# import glob
# target = glob.glob('../static/articles/1/1_*.txt')
# print(target)

# import shutil
# shutil.rmtree('../static/temporary/demo.txt')

# a = 'http://127.0.0.1:5000/static/articles/temporary/img/1593748788.jpg'
# print('/'.join(a.split('/')[3:]))
# print(a.split('/'))
# print(a.split(b))

# import os
# os.rename('../static/articles', '../static/article')

import sys
sys.path.append('../')
from config import config_test_orm
# config_test_orm.initialize_orm()

session = config_test_orm.initialize_orm()['dict_session']
user = config_test_orm.initialize_orm()['dict_user']
comment = config_test_orm.initialize_orm()['dict_comments']
article = config_test_orm.initialize_orm()['dict_Articlelist']

user_1 = session.query(user).filter_by(id = 1).first()
user_2 = session.query(user).filter_by(id = 2).first()
# print(user.nickname)
# print('user_1的评论: ' + str(list(map(lambda x: x.content, user_1.relate_comments))))
# print('user_2的评论: ' + str(list(map(lambda x: x.content, user_2.relate_comments))))

# comment_1 = session.query(comment).filter_by(id = 1).first()
# print(comment_1.relate_article.title)

article_1 = session.query(article).filter_by(id = 1).first()
print(list(map(lambda x: x.content, article_1.relate_comments)))

session.close()

# comment = session.query(comment).filter_by(id = 1).first()
# print(comment.content)
# print(comment.relate_user)