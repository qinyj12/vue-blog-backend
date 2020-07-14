# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify, current_app, session
import os, shutil, time
from orm import orm_get_next_article_id

app = Blueprint('api_save_md_img', __name__)
 
@app.route('/saveimg',methods=['POST'])
def save_img():
    # 判断是不是管理员（id==1）
    session_user_id = session.get('user_id')

    # 如果不是管理员
    if session_user_id != 1:
        abort(401)
    # 如果是管理员
    else:
        # 给当前博客分配id，当前博客应该保存的路径：'./static/articles/1/'
        next_id = orm_get_next_article_id.return_next_article_id()
        current_article_path = current_app.article_path + str(next_id['result']) + '/'

        # 尝试获取图片
        try:
            #获取图片文件 name = file
            img = request.files.get('image')
            #拿到图片原名称，保留后缀名，以时间戳重命名
            img_name = str(round(time.time())) + '.' + img.filename.split('.')[-1]
            # 定义存放图片的路径
            img_path = current_article_path + 'img/'
            #图片path和名称组成图片的保存路径：./static/articles/1/img/dog.jpg
            file_path = img_path + img_name

        # 如果没能成功拿到图片
        except Exception as e:
            current_app.logger.info(e)
            resp = {'status': 500, 'result': '服务器出错了'}
            return jsonify(resp)


        # 如果存在./static/articles/1/img目录，什么都不能做，因为有可能是上一次传入的图片
        if os.path.exists(img_path):
            pass
        # 如果不存在./static/articles/1/img目录，新建他，而且要忽略父级目录来创建他。因为可能不存在./1/
        else:
            os.makedirs(img_path)

        # 尝试保存img
        try:
            #保存图片
            img.save(file_path)
            resp = {'status': 200, 'result': file_path}
            return jsonify(resp)

        # 如果保存失败
        except Exception as e:
            current_app.logger.info(e)
            resp = {'status': 500, 'result': '服务器出错了'}
            return jsonify(resp)