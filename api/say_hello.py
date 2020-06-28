# -*- coding: UTF-8 -*-
from flask import make_response, Blueprint, jsonify

app = Blueprint('say_hello', __name__)

@app.route('/hello', methods = ['GET', 'POST'])
def say_hello():
    resp = {
        'msg': 'hello world',
        'msg2': 'hello dog~'
    }
    return jsonify(resp)
