from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import exists

def initialize_orm():
    Base = declarative_base()
    # User表
    class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key = True, nullable = False)
        nickname = Column(String(20), nullable = False)
        email = Column(String(20), nullable = False)
        password = Column(String(20), nullable = False)
        timestamp = Column(Integer, nullable = False)
        format_updated_time = Column(String(20), nullable = True)
        
    # Mailcode表
    class Mailcode(Base):
        __tablename__ = 'mailcode'
        id = Column(Integer, primary_key = True, nullable = False) # 自增id
        email = Column(String(20), nullable = False) # 给邮箱发送code
        code = Column(String(20), nullable = False) # 四位随机码
        timestamp = Column(Integer, nullable = False) # 录入数据的时间戳
        format_time = Column(String(20), nullable = False) # 格式化时间戳
        if_used = Column(Integer, server_default = '0', nullable = False)
        purpose = Column(String(20), nullable = False)

    # md文章列表
    class Articlelist(Base):
        __tablename__ = 'article_list'
        id = Column(Integer, primary_key = True, nullable = False)
        title = Column(String(20), nullable = False) # 文章标题
        abstract = Column(String(20), nullable = True) # 文章的摘要
        avatar = Column(String(20), nullable = True) # 文章作者的头像
        cover = Column(String(20), nullable = True) # 封面图
        time = Column(String(20), nullable = False) # 文章发布的时间
        views = Column(Integer,  nullable = False) # 文章阅读量
        comments = Column(Integer,  nullable = False) # 文章评论量

    # 这里要注意路径是../datebase/database.db
    engine = create_engine('sqlite:///../database/database.db', connect_args = {'check_same_thread': False})
    DBSession = sessionmaker(engine)
    session = DBSession()

    # return {'dict_session': session, 'dict_user': User, 'dict_mailcode': Mailcode, 'dict_Articlelist': Articlelist}

    return Base.metadata.create_all(engine)