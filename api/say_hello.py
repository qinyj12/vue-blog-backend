# -*- coding: UTF-8 -*-
from flask import make_response, Blueprint, jsonify

app = Blueprint('say_hello', __name__)

@app.route('/hello', methods = ['GET', 'POST'])
def say_hello():
    return 'Hello World!'
