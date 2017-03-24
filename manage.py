# coding: utf8

# import Flask Script object
from flask_script import Manager
import main

# Init manager object via app object
manager = Manager(main.app)
# rewrite the default help arguments
# manager.help_args = ('-?', '--help')

# Create a new commands: runserver
# This command will be run the Flask development_env server
# manager.add_command("runserver", Server())

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=main.app)

if __name__ == '__main__':
    manager.run()
