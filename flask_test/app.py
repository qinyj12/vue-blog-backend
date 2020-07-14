# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from config import config_logger, config_mailcode
from api import (
    api_check_code,
    api_error, 
    api_get_article,
    api_get_session,
    api_login, 
    api_logout, 
    api_mailcode, 
    api_read_article,
    api_reset_password, 
    api_save_article, 
    api_save_md_img,
    api_delete_md_img,
    say_hello, 
    api_signup,
    api_save_cover,
    api_get_comments,
    api_send_comments,
    api_get_board,
    api_send_board
)

app = Flask(__name__)
# 引入flask的配置文件
app.config.from_pyfile('./config/config_flask.py')
# 引入logger的配置文件
app.logger.addHandler(config_logger.initialize_logger())
# 引入邮箱验证码的配置文件
app.mailcode_validity = config_mailcode.Config().validity
app.mailcode_too_often = config_mailcode.Config().too_often
# 引入article所在的路径配置
app.article_path = config_mailcode.Config().article_path
# 引入临时文件夹
app.temporary_path = config_mailcode.Config().temporary_path

# 注册蓝图
app.register_blueprint(api_check_code.app)
app.register_blueprint(api_error.app)
app.register_blueprint(api_get_article.app)
app.register_blueprint(api_get_session.app)
app.register_blueprint(api_login.app)
app.register_blueprint(api_logout.app)
app.register_blueprint(api_mailcode.app)
app.register_blueprint(api_read_article.app)
app.register_blueprint(api_reset_password.app)
app.register_blueprint(api_save_article.app)
app.register_blueprint(api_signup.app)
app.register_blueprint(say_hello.app)
app.register_blueprint(api_save_cover.app)
app.register_blueprint(api_save_md_img.app)
app.register_blueprint(api_delete_md_img.app)
app.register_blueprint(api_get_comments.app)
app.register_blueprint(api_send_comments.app)
app.register_blueprint(api_get_board.app)
app.register_blueprint(api_send_board.app)

CORS(app, supports_credentials=True)

app.run()