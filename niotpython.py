from flask import Flask,request,render_template as render,url_for,redirect
import config
from exts import db
from models import user
app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

@app.route('/')
def index():
	'''
	newuser=user(username="wangwen",password="111111")
	db.session.add(newuser)
	db.session.commit()

	'''
	return render('index.html')
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=="GET":
		return render('login.html')
	elif request.method=="post":
		username=request.form.get('username')
		return "post"
	else:
		return "weizhileixing"
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


if __name__ == '__main__':
	app.run()
