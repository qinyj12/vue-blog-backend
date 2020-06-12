# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import make_response, session

@app.route('/clearsession', methods = ['GET','POST'])
def clear_session():
    resp = make_response()
    
    try:
        session.clear()
        resp.data = 'session cleared'
        return resp

    except Exception as e:
        resp.data = str(e)
        return resp