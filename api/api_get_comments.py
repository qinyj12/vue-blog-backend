# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app
import json
from config import config_orm_initial

orm = config_orm_initial.initialize_orm()
session = orm['dict_session']
Article_list = orm['dict_Articlelist']
user = orm['dict_user']

app = Blueprint('api_get_comments', __name__)

@app.route('/comments/<article_id>', methods = ['POST'])
def get_comments(article_id):
    comments_range = request.form.get('comments_for_single')
    # 尝试把前端传来的参数解析成list
    try:
        temp_list = json.loads(comments_range)

        # 判断参数是否是list，并且只有2个元素
        if isinstance(temp_list, list) and len(temp_list) == 2:
            target_article = session.query(Article_list).filter_by(id = article_id).one()
            # 调用一对多方法
            target_comments = target_article.relate_comments
            comments_in_range = target_comments[temp_list[0]: temp_list[1]]
            resp = list(map(
                lambda x:{
                    'comment':x.content, 
                    'time':x.time, 
                    'user_name':session.query(user).filter_by(id=x.user_id).one().nickname,
                    'user_avatar':session.query(user).filter_by(id=x.user_id).one().avatar
                },
                comments_in_range)
            )

            session.close()
            return jsonify(resp)
        else:
            abort(400)
    except Exception as e:
        current_app.logger.info(e)
        abort(400)