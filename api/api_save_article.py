# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import make_response, session
import datetime
from orm import orm_save_article

@app.route('/savearticle', methods = ['POST'])
def saveArticle():
    resp = make_response()
    # 获取时间、标题、摘要、头像名、md正文
    if request.method == 'POST':
        global inner_time, inner_title, inner_title, inner_abstract, inner_avatar, inner_content
        inner_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        inner_title = request.form.get('title')
        inner_abstract = request.form.get('abstract')
        inner_avatar = request.form.get('avatar')
        inner_content = request.form.get('content')

    else:
        resp.data = 'UNKNOWN METHOD'
        return resp

    # 保存正文id（自增主键）、标题、摘要、头像名、时间到数据库
    inner_result = orm_save_article.save_article(inner_title, inner_abstract, inner_avatar, inner_time)
    resp.data = inner_result
    return resp