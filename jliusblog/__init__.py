# coding: utf8
from flask import Flask, redirect, url_for
from jliusblog.models import db
from jliusblog.controller.blog import blog_blueprint
from jliusblog.controller.main import main_blueprint

def create_app(object_name):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(object_name)
    db.init_app(app)

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)
    app.register_blueprint(main_blueprint)
    return app
