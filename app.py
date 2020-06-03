# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('./config/config_flask.py')
CORS(app)

with app.app_context():
	from api import say_hello
	from api import api_mailcode, api_signup, api_login, api_reset_password
	app.run(host = '0.0.0.0', port = 5000)