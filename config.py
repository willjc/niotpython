import os
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/niot'
DEBUG=True
SQLALCHEMY_TRACK_MODIFICATIONS=True
SECRET_KEY=os.urandom(24)
