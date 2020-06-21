from flask import current_app as app

@app.route('/hello')
def say_hello():
	return 'Hello World!'