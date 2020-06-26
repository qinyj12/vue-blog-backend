# -*- coding: UTF-8 -*-
from flask import session, Blueprint, jsonify

app = Blueprint('api_get_article', __name__)

@app.route('/getarticle', methods = ['GET','POST'])
def get_article():
    if request.method == 'GET':
        articles_range = request.args.get('articles_for_single')
    elif request.method == 'POST':
        articles_range = request.form.get('articles_for_single')
    else:
        pass

    from orm import orm_get_article
    temp_result = orm_get_article.get_article(articles_range)
