
# from test2 import main
# print(main.hello())
# 操作数据库
# import sqlite3
# conn = sqlite3.connect('../database/database.db')
# cursor = conn.cursor()
# cursor.execute('ALTER TABLE user ADD column password INTEGER')
# cursor.execute('ALTER TABLE user RENAME COLUMN name TO nickname')
# cursor.close()
# conn.commit()
# conn.close()
# 获取当前时间
# import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 调用外部接口查找数据库
import sys
sys.path.append('../')
from config import orm_initial

# session = orm_initial.initialize_orm()['dict_session']
# Mailcode = orm_initial.initialize_orm()['dict_mailcode']
# User = orm_initial.initialize_orm()['dict_user']
# a = session.query(Mailcode).filter(Mailcode.email == '156255501@qq.com').all()[-1]

print(orm_initial.initialize_orm())

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
# 	print('try...')
# 	r = 10 / 0
# 	print('result:', r)
# except ZeroDivisionError as e:
# 	print('except:', e)
# finally:
# 	print('finally...')