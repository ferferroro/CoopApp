from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, EqualTo

class UserMaintenanceForm(FlaskForm):
    username = StringField('User Name', render_kw={"placeholder": "User Name"}, validators=[DataRequired()])
    display_name = StringField('Display Name', render_kw={"placeholder": "Display Name"}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Password', render_kw={"placeholder": "Confirm Password"}, validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    uuid = HiddenField('uuid')
    submit_user_add = SubmitField('Save Changes')
    submit_user_update = SubmitField('Save Changes')
    submit_user_delete = SubmitField('Delete')