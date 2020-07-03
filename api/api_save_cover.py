# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify, current_app
import os, shutil

app = Blueprint('api_save_cover', __name__)
 
@app.route('/savecover',methods=['POST'])
def savecover():
    # 判断存不存在temporary目录，如果存在
    if os.path.exists(current_app.temporary_path):
        # 判断存不存在temporary/cover目录，如果存在，删除cover文件夹后，重新创建cover
        if os.path.exists(current_app.temporary_path + 'cover'):
            shutil.rmtree(current_app.temporary_path + 'cover')
            os.mkdir(current_app.temporary_path + 'cover')
        # 如果不存在temporary/cover目录
        else:
            #创建cover目录
            os.mkdir(current_app.temporary_path + 'cover')

    # 如果不存在，创建temporary目录和temporary/cover目录
    else:
        os.mkdir(current_app.temporary_path)
        os.mkdir(current_app.temporary_path + 'cover')

    try:
        #获取图片文件 name = file
        img = request.files.get('file')
        #图片名称，都保存为cover.jpg、cover.png、cover.gif
        img_name = 'cover.' + img.filename.split('.')[-1]
        #图片path和名称组成图片的保存路径
        file_path = current_app.temporary_path + 'cover/' +img_name
        #保存图片
        img.save(file_path)

        resp = {'status': 200, 'result': img_name}
        return jsonify(resp)

    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '服务器出错了'}
        return jsonify(resp)