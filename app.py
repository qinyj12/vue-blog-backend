# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from config import config_logger
from api import say_hello

app = Flask(__name__)
# 引入flask的配置文件
app.config.from_pyfile('./config/config_flask.py')
# 引入logger的配置文件
app.logger.addHandler(config_logger.initialize_logger())
# 注册蓝图
app.register_blueprint(say_hello.app_hello)

CORS(app, supports_credentials=True)

with app.app_context():
    from api import (
        api_mailcode, 
        api_signup, 
        api_login, 
        api_reset_password, 
        api_error, 
        api_get_session, 
        api_logout,
        api_save_article,
        # say_hello
    )
    app.run(host = '0.0.0.0', port = 5000)