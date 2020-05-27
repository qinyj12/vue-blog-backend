# -*- coding: UTF-8 -*-
#engine = create_engine('sqlite:///../database/database.db')
# Base.metadata.create_all(engine)

# 导入:
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

engine = create_engine('sqlite:///database/database.db', connect_args={'check_same_thread': False}) # 因为引用的最上级是app.py，所以路径是相对app.py的
DBSession = sessionmaker(bind = engine)
session = DBSession()

#注册
def sign_up(func_inner_name, func_inner_email, func_inner_password, func_inner_code):
		# 在验证码表里找到这个email
		target = session.query(Mailcode).filter(Mailcode.email == func_inner_email).order_by(Mailcode.timestamp.desc()).all()[0]
		# 如果存在
		if target:
			# 验证用户输入的code是否正确
			if target.code == func_inner_code:
				# 获取当前时间戳
				import time
				func_inner_timestamp = time.time()
				# 判断时间戳是否过期
				if func_inner_timestamp - target.timestamp < 1800:
					# 格式化时间戳
					import datetime
					func_inner_format_time = datetime.datetime.fromtimestamp(func_inner_timestamp)
					session.add(User(nickname = func_inner_name, email = func_inner_email, password = func_inner_password, timestamp = func_inner_timestamp, format_updated_time = func_inner_format_time))
					try:
						session.commit()
						session.close()
						return 'hello world!'
					except Exception as e:
						session.rollback()
						session.close()
						return str(e)
				else:
					# 超期了
					return 'code overdue : %s' % str(time.time() - target.timestamp)
			# 如果验证码不正确
			else:
				return 'code error'
				session.close()
		# 如果验证码表不存在这个email
		else:
			return 'email not found'
			session.close()