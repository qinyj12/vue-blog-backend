from flask import current_app as app
from flask import request, render_template
from flask_mail import Mail, Message
import random
import re
from functools import reduce

@app.route('/mailcode', methods = ['GET','POST'])
def send_mail():
	# 引入上级目录和config
	import sys
	sys.path.append('../')
	from config import config_mail
	app.config.from_object(config_mail.Config())
	# 初始化
	mail = Mail(app)
	# 接收邮箱
	if request.method == 'GET':
		user_mail = request.args.get('email')
	if request.method == 'POST':
		user_mail = request.form.get('email')
	msg = Message('hello world', sender='1562555013@qq.com', recipients=[user_mail])
	list_num = ([random.randint(0,9) for _ in range(4)]) # 4位随机数组成list
	list_str = list(map(lambda x : str(x), list_num)) # 随机数转字符串
	random_num = ''.join(list_str) # 组合字符串
	msg.html = render_template('temp_email.html', name = re.split(r'@', user_mail)[0], code = random_num) # 提取user_mail中@之前的部分
	try:
		mail.send(msg)
		return '已发送至 %s' % user_mail
	except Exception as e:
		return e