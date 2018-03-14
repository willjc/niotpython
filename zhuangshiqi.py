from functools import wraps
from flask import session,redirect,url_for
def login_required(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		userid=session.get('userid')
		if userid==None:
			return redirect(url_for('login'))
		return func(*args,**kwargs)
	return wrapper