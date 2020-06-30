# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app
import json

app = Blueprint('api_get_article', __name__)

@app.route('/getarticle', methods = ['GET','POST'])
def get_article():
    if request.method == 'GET':
        global articles_range
        articles_range = request.args.get('articles_for_single')
    elif request.method == 'POST':
        articles_range = request.form.get('articles_for_single')
    else:
        pass

    # 尝试把前端传来的参数解析成list
    try:
        temp_list = json.loads(articles_range)

        # 判断参数是否是list，并且只有2个元素
        if isinstance(temp_list, list) and len(temp_list) == 2:
            from orm import orm_get_article
            temp_result = orm_get_article.get_article(temp_list)
            return jsonify(temp_result)
        else:
            abort(400)

    except Exception as e:
        current_app.logger.info(e)
        abort(400)
