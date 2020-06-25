# -*- coding: UTF-8 -*-
from flask import make_response, Blueprint, jsonify, current_app

app = Blueprint('say_hello', __name__)

@app.route('/hello', methods = ['GET', 'POST'])
def say_hello():
    resp = {
        'msg': 'hello world',
        'msg2': 'hello dog~'
    }
    current_app.logger.info('say hello')
    return jsonify(resp)
