# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import make_response, session
import json

@app.route('/getsession', methods = ['GET','POST'])
def get_session():
    session_user_id = session.get('user_id')
    session_user_email = session.get('user_email')

    resp = make_response()
    
    try:
        # 如果不为null
        if session_user_email:
            resp.data = json.dumps({'status':200, 'result':session_user_email})
            return resp
        # 如果为null
        else:
            resp.data = json.dumps({'status':404, 'result':session_user_email})
            return resp

    except Exception as e:
        resp.data = json.dumps({'status':500, 'result':str(e)})
        return resp