# -*- coding: UTF-8 -*-
from flask import Blueprint, jsonify, request, abort, current_app

app = Blueprint('api_read_article', __name__)

@app.route('/article/<article_id>')
def read_article(article_id):
    # 拿到博客id后，去目录下找对应的文件名
    import glob
    try:
        target_article_html = glob.glob('./static/articles/'+article_id+'/'+article_id+'_*.html')
        # 如果能找到匹配的文章的话
        if target_article_html:
            # 读取这个文件，记得匹配出来的是个list
            with open(target_article_html[0], encoding='GB2312') as f:
                resp = {'status': 200, 'result': f.read()}
                return jsonify(resp)
        # 如果找不到文章
        else:
            resp = {'status': 404, 'result':'文章失踪了'}
            return jsonify(resp)

    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '服务器出错了'}
        return jsonify(resp)