# -*- coding: UTF-8 -*-
from flask import session, jsonify, Blueprint, current_app

app = Blueprint('api_logout', __name__)

@app.route('/clearsession', methods = ['GET','POST'])
def clear_session():
    # 尝试清理session
    try:
        session.clear()
        resp = {
            'status': 200,
            'result': 'session cleared'
        }
        return jsonify(resp)

    # 如果发生未知错误
    except Exception as e:
        # 把错误写入log
        current_app.logger.info(e)
        resp = {
            'status': 500,
            'result': str(e)
        }
        return jsonify(resp)