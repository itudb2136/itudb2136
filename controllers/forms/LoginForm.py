from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(fieldname='password_confirm', message="Passwords must be the same.")])
    fullname = StringField('Full Name', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password')
    role = RadioField("Role", choices=[("manager", "manager"), ("fan", "fan")])