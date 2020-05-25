# -*- coding: UTF-8 -*-
# Base.metadata.create_all(engine)

# 导入:
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String(20), nullable = False)

engine = create_engine('sqlite:///database/database.db')
DBSession = sessionmaker(bind = engine)
session = DBSession()

#注册
def sign_up(name):
	session.add(User(name = name))
	session.commit()
	session.close()
	return 'hello world!'

def test():
	print('haha')