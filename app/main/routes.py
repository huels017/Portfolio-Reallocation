from flask import render_template, url_for, redirect, flash
from werkzeug.utils import secure_filename
import os
from app.main import bp
from app.main.forms import UploadForm
from app import current_app

from flask_restful import Resource

class TodoItem(Resource):
    def get(self):
        return { 'task': 'stuff', 'things': ['1', '2']}
    def post(self):
        pass

class Portfolio(Resource):

    fake_account_1 = { 'cash': 145, 'crypto': 15, 'stocks': 4500 }
    fake_account_2 = { 'cash': 15, 'crypto': 177, 'stocks': 1234 }
    fake_account_3 = { 'cash': 15, 'crypto': 1555, 'stocks': 16 }

    def get(self):
        return { 'accounts': [ self.fake_account_1, self.fake_account_2, self.fake_account_3 ], 'owner': 'Bob Smith' }

# @bp.route('/')
# @bp.route('/index')
# def index():
# 	return render_template('index.html', title="Welcome!")

# @bp.route('/upload', methods=['GET', 'POST'])
# def upload():
# 	form = UploadForm()
# 	if form.validate_on_submit():
# 		f = form.upload.data
# 		filename = secure_filename(f.filename)
# 		f.save(os.path.join(current_app.instance_path, 'uploads', filename))
# 		flash('File uploaded')
# 		return redirect(url_for('main.index'))
# 	return render_template('upload.html', title='Upload', form=form)