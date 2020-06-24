# -*- coding: UTF-8 -*-
# from flask import current_app as app
from flask import make_response, Blueprint

app_hello = Blueprint('app_hello', __name__)
@app_hello.route('/hello', methods = ['GET', 'POST'])
def say_hello():
    resp = make_response()
    resp.data = 'Hello World!'
    resp.msg = 'yesyesyes'
    return resp


# @app.route('/hello', methods = ['GET', 'POST'])
# def say_hello():
#     resp = make_response()
#     resp.data = 'Hello World!'
#     return resp