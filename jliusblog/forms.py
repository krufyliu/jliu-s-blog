from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from jliusblog.models import User


class CommentForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    text = TextField('Comment', validators=[DataRequired(), Length(max=255)])

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('PassWord', validators=[DataRequired()])

    def validate(self):
        valid = super(LoginForm, self).validate()
        if not valid:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user or not user.validate_password(self.password.data):
            self.username.errors.append('Invalid username or password.')
            return False

        return True

class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    def validate(self):
        valid = super(RegisterForm, self).validate()
        if not valid:
            return False

        if User.query.filter_by(username=self.username.data).first():
            self.username.errors.append('username has already existed.')
            return False

        if User.query.filter_by(email=self.email.data).first():
            self.username.errors.append('email has already existed')
            return False

        return True

class PostNewForm(Form):
    title = StringField('Title', validators=[DataRequired(), Length(max=255)])
    text = TextAreaField('Text', validators=[DataRequired()])
