from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired

# TODO: ValidationErrors, registration, forgot password
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "username"})
	password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
	submit = SubmitField('Log in')