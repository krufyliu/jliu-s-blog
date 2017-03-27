from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length, Email


class CommentForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    text = TextField('Comment', validators=[DataRequired(), Length(max=255)])