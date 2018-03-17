from flask import Flask,request,render_template as render,url_for,redirect,session
import config
from exts import db

from models import user
from functools import wraps
app = Flask(__name__)
app.config.from_object(config)

app.jinja_env.variable_start_string = '<{'
app.jinja_env.variable_end_string = '}>'

db.init_app(app)
##
##判断登录状态的装饰器
##
from zhuangshiqi import login_required

@app.route('/')
def index():
	return render('index.html')
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=='POST':
		lusername=request.form.get('username')
		lpassword=request.form.get('password')
		#print(lpassword)

		userdata=user.query.filter(user.username==lusername,user.password==lpassword).first()#这里面要用双等号ls#
		if userdata:
			session['userid']=userdata.id
			return redirect(url_for('guanli'))
	else:
		return render('login.html')
	#return username
@app.route('/register/',methods=['GET','POST'])
def register():
	if request.method=='GET':
		return render('register.html')
	elif request.method=='POST':
		userpost=request.form.get('username')
		passwordpost=request.form.get('password')
		rpassword=request.form.get('rpassword')
		if userpost and passwordpost and rpassword:
			if passwordpost!=rpassword :
				return '两次密码不相等'
			else:
				newuser=user(username=userpost,password=passwordpost)
				db.session.add(newuser)
				a= db.session.commit()
				return redirect(url_for('login'))

		else:
			return '信息不能为空'
@app.route('/guanli/')
@login_required
def guanli():
	return render('guanli.html')
# @app.route('/base')
# def base():
# 	return render('base.html')

if __name__ == '__main__':
	app.run()
