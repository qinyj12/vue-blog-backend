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
            # 先找到对应的article
            target_article = session.query(Article_list).filter_by(id = article_id).one_or_none()
            # 如果能找到这篇文章
            if target_article:
                # 然后调用一对多方法，拿到这篇article对应的comments和comments总数
                target_comments = target_article.relate_comments
                # 拿到的结果和list差不多，所以取倒数排序
                comments_in_range = target_comments[-1-temp_list[0] : -1-temp_list[1]: -1]
                comments_count = len(target_comments)
                comments_list = list(map(
                    lambda x:{
                        'comment':x.content, 
                        'time':x.time, 
                        'user_name':session.query(user).filter_by(id=x.user_id).one().nickname,
                        'user_avatar':session.query(user).filter_by(id=x.user_id).one().avatar
                    },
                    comments_in_range)
                )
                resp = {'status': 200, 'result': {'count': comments_count, 'commentsList': comments_list}}
                session.close()
                return jsonify(resp)
            # 如果不能找到这篇文章
            else:
                abort(400)
        else:
            abort(400)
    except Exception as e:
        current_app.logger.info(e)
        abort(400)