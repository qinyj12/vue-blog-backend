from flask import Flask

app = Flask(__name__)

with app.app_context():
	from api import say_hello
	from api import mail_code, register
	app.run(host = '0.0.0.0', debug = True, port = 5000)