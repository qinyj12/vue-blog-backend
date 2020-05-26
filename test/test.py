
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
# from sqlalchemy import Column, String, Integer, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.sql import exists

# Base = declarative_base()

# class User(Base):
# 	__tablename__ = 'user'
# 	id = Column(Integer, primary_key = True, nullable = False)
# 	nickname = Column(String(20), nullable = False)
# 	email = Column(String(20), nullable = False)
# 	password = Column(String(20), nullable = False)
# 	updated_time = Column(String(20), nullable = True)

# class Mailcode(Base):
# 	__tablename__ = 'mailcode'
# 	id = Column(Integer, primary_key = True, nullable = False)
# 	email = Column(String(20), nullable = False)
# 	code = Column(String(20), nullable = False)
# 	updated_time = Column(String(20), nullable = True)


# engine = create_engine('sqlite:///../database/database.db')
# DBSession = sessionmaker(bind = engine)
# session = DBSession()

# a = session.query(User).filter(User.nickname == 'firstman').first()
# if a:
# 	print(a.id)
# 	session.close()
# else:
# 	print('not found')
# 	session.close()
