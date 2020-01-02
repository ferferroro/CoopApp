from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField('Login')