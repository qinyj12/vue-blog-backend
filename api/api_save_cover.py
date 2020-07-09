# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify, current_app
import os, shutil, time
from orm import orm_get_next_article_id

app = Blueprint('api_save_cover', __name__)

@app.route('/savecover',methods=['POST'])
def savecover():

    # 给当前博客分配id，当前博客应该保存的路径：'./static/articles/1/'
    next_id = orm_get_next_article_id.return_next_article_id()
    current_article_path = current_app.article_path + str(next_id['result']) + '/'
    
    # 尝试获取图片
    try:
        #获取图片文件 name = file
        img = request.files.get('file')
        #图片名称，都保存为cover.jpg、cover.png、cover.gif
        img_name = 'cover.' + img.filename.split('.')[-1]
        # 定义存放cover的路径
        cover_path = current_article_path + 'cover/'
        #图片path和名称组成图片的保存路径：./static/articles/1/cover/cover.jpg
        file_path = cover_path + img_name

    # 如果没能成功拿到图片
    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '服务器出错了'}
        return jsonify(resp)

    # 如果存在./static/articles/1/cover目录，先清空他
    if os.path.exists(cover_path):
        shutil.rmtree(cover_path)
        # 因为要给他时间放开句柄
        time.sleep(0.00000001)
        os.mkdir(cover_path)

    # 如果不存在./static/articles/1/cover，创建他，而且要忽略父级目录来创建他
    else:
        os.makedirs(cover_path)

    # 尝试保存cover
    try:
        #保存图片
        img.save(file_path)
        resp = {'status': 200, 'result': img_name}
        return jsonify(resp)

    # 如果保存失败
    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '服务器出错了'}
        return jsonify(resp)
