# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app
import json
from config import config_orm_initial

orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
board = orm['dict_board']
user = orm['dict_user']

app = Blueprint('api_get_board', __name__)

@app.route('/board', methods = ['POST'])
def get_board():
    board_range = request.form.get('comments_for_single')
    # 尝试把前端传来的参数解析成list
    try:
        temp_list = json.loads(board_range)

        # 判断参数是否是list，并且只有2个元素
        if isinstance(temp_list, list) and len(temp_list) == 2:
            target_board = session.query(board).all()
            # 取倒序
            board_in_range = target_board[-1-temp_list[0] : -1-temp_list[1]: -1]
            board_count = len(target_board)
            board_list = list(map(
                lambda x:{
                    'comment':x.content, 
                    'time':x.time, 
                    'user_name':session.query(user).filter_by(id=x.user_id).one().nickname,
                    'user_avatar':session.query(user).filter_by(id=x.user_id).one().avatar
                },
                board_in_range)
            )
            resp = {'status': 200, 'result': {'count': board_count, 'boardList': board_list}}
            session.close()
            return jsonify(resp)
        else:
            abort(400)
    except Exception as e:
        current_app.logger.info(e)
        abort(400)