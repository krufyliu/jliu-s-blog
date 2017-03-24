# coding: utf8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic'
    )

    def __str__(self):
        return '<User `{}`>'.format(self.username)

posts_tags = db.Table('posts_tags',
   db.Column('post_id', db.Integer),
   db.Column('tag_id', db.Integer))

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False, default="")
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    publish_at = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    tags = db.relationship('Tag', 
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic'),
        lazy='dynamic')

    def __str__(self):
        return '<Post `{}`'.format(self.title)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return '<Tag `{}`'.format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    post_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return '<Comment for `post {}`>'.format(self.post_id)


