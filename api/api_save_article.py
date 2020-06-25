# -*- coding: UTF-8 -*-
from flask import session, request, Blueprint, jsonify, current_app
import datetime

app = Blueprint('api_save_article', __name__)

@app.route('/savearticle', methods = ['POST'])
def saveArticle():
    # 获取时间、标题、摘要、头像名、md正文
    if request.method == 'POST':
        global parameter_time, parameter_title, parameter_abstract, parameter_avatar, parameter_content
        parameter_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        parameter_title = request.form.get('title')
        parameter_abstract = request.form.get('abstract')
        parameter_avatar = request.form.get('avatar')
        parameter_content = request.form.get('content')
    # 因为本来就不允许其他方法，所以直接pass也没关系
    else:
        pass

    # 保存正文id（自增主键）、标题、摘要、头像名、时间到数据库
    from orm import orm_save_article
    temp_result = orm_save_article.save_article(parameter_title, parameter_abstract, parameter_avatar, parameter_time)

    # 如果接口返回的状态码正常
    if temp_result == 200:
        return jsonify(temp_result)
    # 如果接口返回的状态码异常
    else:
        current_app.logger.info(temp_result['result'])
        return jsonify(temp_result)