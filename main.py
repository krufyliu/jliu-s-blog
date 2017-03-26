# coding: utf8
from flask import Flask

import config

app = Flask(__name__)

app.config.from_object(config)

import views

if __name__ == '__main__':
    # Entry the application 
    app.run()
