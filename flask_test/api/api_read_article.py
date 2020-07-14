# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app

app = Blueprint('api_read_article', __name__)

@app.route('/article/<article_id>')
def read_article(article_id):
    # 拿到博客id后，去目录下找对应的文件名
    import glob
    try:
        target_article_html = glob.glob('./static/articles/'+article_id+'/'+article_id+'_*.html')[0]

        # 读取这个文件
        with open(target_article_html) as f:
            resp = {'status': 200, 'result': f.read()}
            return jsonify(resp)

    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '没有找到文章'}
        return jsonify(resp)
