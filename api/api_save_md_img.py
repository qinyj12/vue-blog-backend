# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify, current_app
import os, shutil, time

app = Blueprint('api_save_md_img', __name__)
 
@app.route('/saveimg',methods=['POST'])
def save_img():
    # 判断存不存在temporary目录，如果存在
    if os.path.exists(current_app.temporary_path):
        # 判断存不存在temporary/img目录，如果存在，啥都不能干，因为不能删除内部的文件
        if os.path.exists(current_app.temporary_path + 'img'):
            pass
        # 如果不存在temporary/img目录
        else:
            #创建img目录
            os.mkdir(current_app.temporary_path + 'img')

    # 如果不存在，创建temporary目录和temporary/img目录
    else:
        os.mkdir(current_app.temporary_path)
        os.mkdir(current_app.temporary_path + 'img')

    try:
        #获取图片文件 name = file
        img = request.files.get('image')
        #拿到图片原名称
        img_name = img.filename
        #拿到图片的后缀名，以时间戳重命名，保存到temporary/img目录
        part_of_path = 'img/' + str(round(time.time())) + '.' + img_name.split('.')[-1]
        file_path = current_app.temporary_path + part_of_path
        #保存图片
        img.save(file_path)

        resp = {'status': 200, 'result': file_path}
        return jsonify(resp)

    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '服务器出错了'}
        return jsonify(resp)