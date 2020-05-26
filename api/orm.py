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
	updated_time = Column(String(20), nullable = True)

class Mailcode(Base):
	__tablename__ = 'mailcode'
	id = Column(Integer, primary_key = True, nullable = False)
	email = Column(String(20), nullable = False)
	code = Column(String(20), nullable = False)
	updated_time = Column(Integer, nullable = False)

engine = create_engine('sqlite:///database/database.db', connect_args={'check_same_thread': False}) # 因为引用的最上级是app.py，所以路径是相对app.py的
DBSession = sessionmaker(bind = engine)
session = DBSession()

#注册
def sign_up(nickname, email, password, code):
		# 在验证码表里找到这个email
		target_code = session.query(Mailcode).filter(Mailcode.email == email).first()
		# 如果存在
		if target_code:
			# 验证用户输入的code是否正确
			if target_code.code == code:
				# 判断验证码是否过期（30min）
				import time
				if time.time() - target_code.updated_time < 1800:
					import datetime
					updated_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					session.add(User(nickname = nickname, email = email, password = password, updated_time = updated_time))
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
					return 'code overdue : %s' % str(time.time() - target_code.updated_time)
			# 如果验证码不正确
			else:
				return 'code error'
				session.close()
		# 如果验证码表不存在这个email
		else:
			return 'email not found'
			session.close()