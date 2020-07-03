# -*- coding: UTF-8 -*-
from flask import session, Blueprint, jsonify, current_app

app = Blueprint('api_get_session', __name__)

@app.route('/getsession', methods = ['GET','POST'])
def get_session():

    session_user_id = session.get('user_id')
    session_user_email = session.get('user_email')

    # try:
        # 如果成功解析浏览器session
    if session_user_email:
        from orm import orm_get_user_info
        user_info_got = orm_get_user_info.get_user_info(session_user_id)
        return jsonify(user_info_got)

    # 如果浏览器session解析失败
    else:
        resp = {
            'status': 400,
            'result': '未登录'
        }
        return jsonify(resp)

    # 如果发生了未知的错误
    # except Exception as e:
    #     # 把错误保存到log里
    #     current_app.logger.info(e)
    #     resp = {
    #         'status': 500,
    #         'result': str(e)
    #     }
    #     return jsonify(resp)