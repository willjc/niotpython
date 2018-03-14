from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from niotpython import app
from exts import db
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.command
def nihao():
	print('nihaoa')
if __name__=='__main__':
	manager.run()