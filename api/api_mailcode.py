from flask import current_app as app
from flask import request, render_template
from flask_mail import Mail, Message
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

	# 接收邮箱，和目的
	if request.method == 'GET':
		user_mail = request.args.get('email')
		user_purpose = request.args.get('purpose')
	if request.method == 'POST':
		user_mail = request.form.get('email')
		user_purpose = request.form.get('purpose')

	msg = Message('hello world', sender='1562555013@qq.com', recipients=[user_mail])

	# 引入外部模块，存储验证码到数据库
	from orm import orm_code
	func_inner_result = orm_code.save_mail_code(user_mail, user_purpose)

	# 尝试把返回的结果转成int，如果成功的话，证明就是4位验证码
	try:
		int(func_inner_result)
		msg.html = render_template('temp_email.html', name = re.split(r'@', user_mail)[0], code = func_inner_result) # 提取user_mail中@之前的部分
		# 发邮件
		try:
			mail.send(msg)
			return '已发送至 %s' % user_mail
		# 有可能邮箱配置会出现问题
		except Exception as e:
			return str(e)
	
	except:
		return func_inner_result