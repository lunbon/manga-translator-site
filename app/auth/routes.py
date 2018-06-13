from app import app, db
from flask import render_template, redirect, url_for,request
from app.auth.forms import LoginForm
from flask_login import current_user, login_user, login_required,logout_user
from app.models import User

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			return redirect(url_for('auth.login'))
		login_user(user, remember=False)
		return redirect(url_for('index'))
	return render_template('auth/login.html', title='Sign in', form=form)