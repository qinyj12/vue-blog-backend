from flask import current_app as app
from flask import request

@app.route('/register', methods = ['GET','POST'])
def register():
	if request.method == 'GET':
		nickname = request.args.get('nickname')
		email = request.args.get('email')
		password = request.args.get('password')
		mailcode = request.args.get('code')
	if request.method == 'POST':
		nickname = request.form.get('nickname')
		email = request.form.get('email')
		password = request.form.get('password')
		mailcode = request.form.get('code')
	from api import orm
	return(orm.sign_up(nickname, email, password, mailcode))