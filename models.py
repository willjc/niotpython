from exts import db
class user(db.Model):
	id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
	username=db.Column(db.String(100),nullable=False)
	password=db.Column(db.String(32),nullable=True)
