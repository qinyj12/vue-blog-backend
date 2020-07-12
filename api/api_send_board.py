# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app
import datetime
from config import config_orm_initial

orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
board = orm['dict_board']

app = Blueprint('api_send_board', __name__)

@app.route('/sendboard', methods = ['POST'])
def send_board():
    temp_comment = request.form.get('comment')
    temp_user_id = request.form.get('usid')
    temp_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    new_comment = board(
        content = temp_comment,
        time = temp_time,
        user_id = temp_user_id
    )
    try:
        session.add(new_comment)
        session.commit()
        session.close()
        resp = {'status': 200, 'result': '留言成功'}
        return jsonify(resp)

    except Exception as e:
        current_app.logger.info(e)
        session.rollback()
        session.close()
        abort(500)