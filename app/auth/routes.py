from flask import render_template, url_for, redirect, flash
from app.auth import bp
from app.auth.forms import LoginForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested')
		return redirect(url_for('main.index'))
	return render_template('auth/login.html', title='Log In', form=form)
