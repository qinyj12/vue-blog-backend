# -*- coding: UTF-8 -*-
from flask import current_app as app
from flask import request

@app.route('/resetpass', methods = ['GET','POST'])
def reset_password():
    if request.method == 'GET':
        email = request.args.get('email')
        mailcode = request.args.get('code')
        new_pass = request.args.get('new_pass')
    if request.method == 'POST':
        email = request.form.get('email')
        mailcode = request.form.get('code')
        new_pass = request.form.get('new_pass')
    from orm import orm_reset_pass
    return(orm_reset_pass.reset_password(email, mailcode, new_pass))