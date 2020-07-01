 
from flask import request, Blueprint, jsonify, current_app

app = Blueprint('api_save_cover', __name__)
 
@app.route('/savecover',methods=['POST'])
def savecover():
    try:
        #获取图片文件 name = file
        img = request.files.get('file')

        #图片名称
        img_name = img.filename
        #图片path和名称组成图片的保存路径
        file_path = current_app.temporary_path + img_name
        #保存图片
        img.save(file_path)

        resp = {'status': 200, 'result': img_name}
        return jsonify(resp)

    except Exception as e:
        current_app.logger.info(e)
        resp = {'status': 500, 'result': '服务器出错了'}
        return jsonify(resp)