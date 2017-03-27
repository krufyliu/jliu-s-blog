from flask import Blueprint, request, flash, url_for, redirect, render_template
from jliusblog.forms import RegisterForm, LoginForm
from jliusblog.models import db, User

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       flash('You have been logined in.', category='success') 
       return redirect(url_for('blog.home'))
    return render_template('login.html', form=form)

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your user has been created, please login', category='success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)
