# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify

app = Blueprint('api_error', __name__)

@app.app_errorhandler(404)
def handle_404_error(error):  # error：错误信息
    resp = {'stauts': 404, 'result': '404 找不到资源哦'}
    return jsonify(resp)

@app.app_errorhandler(401)
def handle_401_error(error):  # error：错误信息
    resp = {'stauts': 401, 'result': '有内鬼终止交易'}
    return jsonify(resp)

@app.app_errorhandler(500)
def handle_500_error(error):  # error：错误信息
    resp = {'stauts': 500, 'result': '服务器出错了'}
    return jsonify(resp)