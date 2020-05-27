
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
# 查找数据库中的数据
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import exists

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True, nullable = False)
	nickname = Column(String(20), nullable = False)
	email = Column(String(20), nullable = False)
	password = Column(String(20), nullable = False)
	timestamp = Column(Integer, nullable = False)
	format_updated_time = Column(String(20), nullable = True)

class Mailcode(Base):
	__tablename__ = 'mailcode'
	id = Column(Integer, primary_key = True, nullable = False) # 自增id
	email = Column(String(20), nullable = False) # 给邮箱发送code
	code = Column(String(20), nullable = False) # 四位随机码
	timestamp = Column(Integer, nullable = False) # 录入数据的时间戳
	format_time = Column(String(20), nullable = False) # 格式化时间戳

engine = create_engine('sqlite:///../database/database.db', connect_args={'check_same_thread': False})
DBSession = sessionmaker(engine)
session = DBSession()

a = session.query(Mailcode).filter(Mailcode.email == '1562555013@qq.com').order_by(Mailcode.timestamp.desc()).all()
if a:
	print(a[0].timestamp)
	session.close()
else:
	print('not found')
	session.close()
# 转换时间戳
# import time, datetime
# timeStamp = 1590506090
# dateArray = datetime.datetime.fromtimestamp(timeStamp)
# print(dateArray)
