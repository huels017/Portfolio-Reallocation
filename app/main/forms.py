from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

EXCEL_FILE_EXTENSIONS = ['xls', 'xlt', 'xlsx', 'xlsm', 'xltx', 'xltm', 'xlsb', 'xlw']

class UploadForm(FlaskForm):
	upload = FileField('upload', validators=[FileRequired(), FileAllowed(EXCEL_FILE_EXTENSIONS, 'Only Excel files are allowed')])
	submit = SubmitField('Submit')