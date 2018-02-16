from flask import render_template, url_for, redirect, flash
from werkzeug.utils import secure_filename
import os
from app.main import bp
from app.main.forms import UploadForm
from app import current_app


@bp.route('/')
@bp.route('/index')
def index():
	return render_template('index.html', title="Welcome!")

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
	form = UploadForm()
	if form.validate_on_submit():
		f = form.upload.data
		filename = secure_filename(f.filename)
		f.save(os.path.join(current_app.instance_path, 'uploads', filename))
		flash('File uploaded')
		return redirect(url_for('main.index'))
	return render_template('upload.html', title='Upload', form=form)