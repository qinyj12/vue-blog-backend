from flask import current_app as app
from flask_mail import Mail, Message
import random
from functools import reduce

# 引入上级目录
import sys
sys.path.append('../')
# 引入config/config_mail.py
from config import config_mail
# 引入flask_mail的配置文件
app.config.from_object(config_mail.Config())
# 初始化
mail = Mail(app)
# 发送邮件接口
@app.route('/sendmail', strict_slashes = False)
def send_mail():
    msg = Message('hello world', sender='1562555013@qq.com', recipients=['qinyj12@126.com'])
    list_num = ([random.randint(0,9) for _ in range(4)])
    def to_str(x):
    	return str(x)
    list_str = list(map(to_str, list_num))
    random_num = ''.join(list_str)
    msg.body = random_num
    mail.send(msg)
    return '邮件发送成功！'

