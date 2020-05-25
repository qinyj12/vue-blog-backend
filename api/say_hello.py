from flask import current_app as app


@app.route('/hello/<user_name>')
def say_hello(user_name):
	from api import orm
	return(orm.sign_up(user_name))