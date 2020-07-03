# -*- coding: UTF-8 -*-
from flask import request, Blueprint, jsonify, current_app
import os

app = Blueprint('api_delete_md_img', __name__)

@app.route('/deleteimg',methods=['POST'])
def delete_img():
    # http://127.0.0.1:5000/static/articles/temporary/img/1593748788.jpg
    temp = request.form.get('imgUrl')
    target_img = '/'.join(temp.split('/')[3:])
    # 尝试删除target_img
    try:
        os.remove(target_img)
    # 如果删除出错，一般就是找不到target_img
    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '服务器找不到文件，就当删除成功了吧'}
        return jsonify(resp)

    resp = {'status': 200, 'result': '图片已删除'}
    return jsonify(resp)