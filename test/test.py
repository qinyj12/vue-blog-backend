
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
import time
import sys
sys.path.append('../')
from config import config_test_orm
from sqlalchemy import exists, and_, or_
session = config_test_orm.initialize_orm()['dict_session']
Mailcode = config_test_orm.initialize_orm()['dict_mailcode']
User = config_test_orm.initialize_orm()['dict_user']

email = 'qinyj12@126.com'


target_code_list = session.query(Mailcode).filter(
    Mailcode.email == 'qinyj12@126.com',
    # Mailcode.purpose == 'reset_password',
    Mailcode.if_used == 0,
    time.time() - Mailcode.timestamp < 180000
).all()

if target_code_list:
    print('yes')
else:
    print('no')
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
