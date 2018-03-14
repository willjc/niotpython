from flask import Flask
import config
from exts import db
from models import user
app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

@app.route('/')
def hello_world():
	newuser=user(username="wangwen",password="111111")
	db.session.add(newuser)
	db.session.commit()
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
