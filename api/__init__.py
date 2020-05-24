from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
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
@app.route('/', strict_slashes = False)
def register():
    msg = Message('hello world', sender='1562555013@qq.com', recipients=['qinyj12@126.com'])
    msg.body = 'hello world!'
    mail.send(msg)
    return '邮件发送成功！'

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000)