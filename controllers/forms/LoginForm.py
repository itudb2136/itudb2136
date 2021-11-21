from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo(fieldname='password_confirm')])
    fullname = StringField('fullname', validators=[DataRequired()])
    password_confirm = PasswordField('password_confirm')
    role = SelectField("role", choices=[("manager", "manager"), ("fan", "fan")])
    submit = SubmitField('login')