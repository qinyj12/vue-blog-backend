# -*- coding: UTF-8 -*-
from flask import current_app as app

@app.errorhandler(404)
def handle_404_error(error):  # error：错误信息
    return "404 找不到资源哦"