# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app, session
import datetime
from config import config_orm_initial

orm = config_orm_initial.initialize_orm()
orm_session = orm['dict_session']
orm_board = orm['dict_board']

app = Blueprint('api_send_board', __name__)

@app.route('/sendboard', methods = ['POST'])
def send_board():
    # 如果session能被解析出来
    if session.get('user_id'):
        temp_comment = request.form.get('comment')
        temp_user_id = request.form.get('usid')
        temp_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        new_comment = orm_board(
            content = temp_comment,
            time = temp_time,
            user_id = temp_user_id
        )
        try:
            orm_session.add(new_comment)
            orm_session.commit()
            orm_session.close()
            resp = {'status': 200, 'result': '留言成功'}
            return jsonify(resp)

        except Exception as e:
            current_app.logger.info(e)
            orm_session.rollback()
            orm_session.close()
            abort(500)

    # 如果session解析不出来
    else:
        orm_session.close()
        abort(401)