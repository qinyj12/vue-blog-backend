# -*- coding: UTF-8 -*-
from flask import session, request, Blueprint, jsonify, current_app, abort
import datetime

app = Blueprint('api_save_article', __name__)

@app.route('/savearticle', methods = ['POST'])
def saveArticle():
    # 判断是不是管理员（id==1）
    session_user_id = session.get('user_id')
    if session_user_id != 1:
        abort(401)

    else:
        # 获取时间、标题、摘要、头像名、md正文
        if request.method == 'POST':
            global parameter_time, parameter_title, parameter_abstract, parameter_avatar, parameter_content, parameter_cover
            parameter_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            parameter_title = request.form.get('title')
            parameter_abstract = request.form.get('abstract')
            parameter_avatar = request.form.get('avatar')
            parameter_content = request.form.get('content')
            parameter_cover = request.form.get('cover')
        # 因为本来就不允许其他方法，所以直接pass也没关系
        else:
            pass

        # 保存正文id（自增主键）、标题、摘要、头像名、时间到数据库
        from orm import orm_save_article
        temp_result = orm_save_article.save_article(parameter_title, parameter_abstract, parameter_avatar, parameter_cover, parameter_time)

        # 如果状态码正常，
        if temp_result['status'] == 200:

            try:
                # 尝试把temp目录里的图片移动到covers目录
                import shutil, os.path
                source_img = './static/images/temp/' + parameter_cover
                target_img = './static/images/covers/' + '[' + str(temp_result['result']['article_id']) + ']' + parameter_cover

                # 判断temp目录里有没有这个图片，如果有
                if os.path.isfile(source_img):
                    # 把图片移动到covers目录，并重命名
                    shutil.move(source_img, target_img)

                # 如果没有
                else:
                    from orm import orm_delete_article
                    temp_delete_result = orm_delete_article.delete_article(temp_result['result']['article_id'])
                    resp = {'status': 500, 'result': '图片没有上传成功，所以写入又删除'}
                    return jsonify(resp)

                # 尝试保存content为md格式
                file_name = './static/articles/' + '[' + str(temp_result['result']['article_id']) + ']' + parameter_title + '.md'
                with open(file_name , 'w') as f:
                    f.write(parameter_content)

                return jsonify(temp_result)

            # 如果发生意想不到的错误
            except Exception as e:
                current_app.logger.info(e)
                # 把article表的那个数据删除
                from orm import orm_delete_article
                temp_delete_result = orm_delete_article.delete_article(temp_result['result']['article_id'])

                resp = {
                    'status': 500,
                    'result': '写入又删除，啥也没干成'
                }
                return jsonify(resp)

        # 如果状态码不正常，即没有成功保存到articl表里，那就没必要存md了
        else:
            return temp_result