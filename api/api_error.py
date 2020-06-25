# -*- coding: UTF-8 -*-
from flask import Blueprint

app = Blueprint('api_error', __name__)

@app.errorhandler(404)
def handle_404_error(error):  # error：错误信息
    return "404 找不到资源哦"