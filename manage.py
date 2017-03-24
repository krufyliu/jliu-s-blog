# coding: utf8

# import Flask Script object
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import app
import models

# Init manager object via app object
manager = Manager(app)
# rewrite the default help arguments
# manager.help_args = ('-?', '--help')

# Create a new commands: runserver
# This command will be run the Flask development_env server
# manager.add_command("runserver", Server())

# Init migrate
migrate = Migrate(app, models.db)

manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(
        app=app,
        db=models.db,
        User=models.User,
        Post=models.Post,
        Comment=models.Comment,
        Tag=models.Tag)

if __name__ == '__main__':
    manager.run()
