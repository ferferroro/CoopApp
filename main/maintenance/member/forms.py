from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired
from wtforms.widgets import html5
from wtforms.fields.html5 import DateField

class MemberMaintenanceForm(FlaskForm):
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    first_name = StringField('Fist Name', render_kw={"placeholder": "Fist Name"}, validators=[DataRequired()])
    last_name = StringField('Last Name', render_kw={"placeholder": "Last Name"}, validators=[DataRequired()])
    address = StringField('Address', render_kw={"placeholder": "Address"}, validators=[DataRequired()])
    phone = StringField('Phone', render_kw={"placeholder": "Phone"}, validators=[DataRequired()])
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile"}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    monthly_contribution = FloatField('Monthly Contribution', widget=html5.NumberInput(), render_kw={"placeholder": "Monthly Contribution"}, validators=[DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d', render_kw={"onkeydown": "return false"}, validators=[DataRequired()])
    uuid = HiddenField('uuid')
    submit_member_add = SubmitField('Create')
    submit_member_update = SubmitField('Update')
    submit_member_delete = SubmitField('Delete')
    submit_member_back= SubmitField('Back')

        

