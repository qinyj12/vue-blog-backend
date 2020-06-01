# -*- coding: UTF-8 -*-
from flask import Flask

app = Flask(__name__)

with app.app_context():
	from api import say_hello
	from api import api_mailcode, api_signup, api_login, api_reset_password
	app.run(host = '0.0.0.0', debug = True, port = 5000)