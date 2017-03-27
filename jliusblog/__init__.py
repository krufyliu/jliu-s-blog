# coding: utf8
from flask import Flask, redirect, url_for
from jliusblog.models import db
from jliusblog.controller.blog import blog_blueprint

import config

app = Flask(__name__.split('.')[0])

app.config.from_object(config)


db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('blog.home'))

app.register_blueprint(blog_blueprint)

if __name__ == '__main__':
    # Entry the application 
    app.run()
