# -*- coding: UTF-8 -*-
from flask import session, request, Blueprint, jsonify, current_app, abort
import datetime, os, shutil

app = Blueprint('api_save_article', __name__)

@app.route('/savearticle', methods = ['POST'])
def saveArticle():
    # 判断是不是管理员（id==1）
    session_user_id = session.get('user_id')

    # 如果不是管理员
    if session_user_id != 1:
        abort(401)

    # 如果是管理员
    else:
        # 获取时间、标题、摘要、头像名、md正文
        if request.method == 'POST':
            global parameter_time, parameter_title, parameter_abstract, parameter_avatar, parameter_content, parameter_cover
            parameter_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            parameter_title = request.form.get('title')
            parameter_abstract = request.form.get('abstract')
            parameter_avatar = request.form.get('avatar')
            parameter_md = request.form.get('content_md')
            parameter_html = request.form.get('content_html')
            parameter_cover = request.form.get('cover')
        # 因为本来就不允许其他方法，所以直接return也没关系
        else:
            return

        # 保存正文id（自增主键）、标题、摘要、头像名、时间到数据库
        from orm import orm_save_article
        temp_result = orm_save_article.save_article(parameter_title, parameter_abstract, parameter_avatar, parameter_cover, parameter_time)

        # 如果文章信息成功保存到数据库
        if temp_result['status'] == 200:
            try:
                # 尝试保存parameter_md为md格式。temp_result['result']就是article的id
                md_path = current_app.article_path + str(temp_result['result']) + '/'
                md_filename = str(temp_result['result']) + '_' + parameter_title + '.md'
                with open(md_path + md_filename, 'w') as f:
                    f.write(parameter_md)

                # 尝试保存parameter_html为html格式
                html_path = current_app.article_path + str(temp_result['result']) + '/'
                html_filename = str(temp_result['result']) + '_' + parameter_title + '.html'
                with open(html_path + html_filename, 'w') as f:
                    f.write(parameter_html)

                resp = {'status': 200, 'result': '保存成功'}
                return jsonify(resp)

            # 如果出错的话，删除数据库记录，和这个article_id的目录
            except Exception as e:
                current_app.logger.info(e)
                from orm import orm_delete_article
                temp_delete_result = orm_delete_article.delete_article(temp_result['result'])
                resp = {'status': 500, 'result': '写入又删除，啥也没干成'}
                return jsonify(resp)

        # 如果状态码不正常，即没有成功保存到articl表里，直接返回
        else:
            return jsonify(temp_result)