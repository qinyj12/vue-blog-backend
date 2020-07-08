# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app
import json

app = Blueprint('api_get_comments', __name__)

@app.route('/comments/<article_id>', methods = ['POST'])
def get_comments(article_id):
    comments_range = request.form.get('comments_for_single')
    # 尝试把前端传来的参数解析成list
    try:
        temp_list = json.loads(comments_range)

        # 判断参数是否是list，并且只有2个元素
        if isinstance(temp_list, list) and len(temp_list) == 2:
            from orm import orm_get_comments
            temp_result = orm_get_comments.get_comments(article_id, temp_list)
            return jsonify(temp_result)
        else:
            abort(400)
    except Exception as e:
        current_app.logger.info(e)
        abort(400)