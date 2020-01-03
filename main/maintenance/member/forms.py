from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class MemberMaintenanceForm(FlaskForm):
    first_name = StringField('Fist Name', render_kw={"placeholder": "Fist Name"}, validators=[DataRequired()])
    last_name = StringField('Last Name', render_kw={"placeholder": "Last Name"}, validators=[DataRequired()])
    address = StringField('Address', render_kw={"placeholder": "Address"}, validators=[DataRequired()])
    phone = StringField('Phone', render_kw={"placeholder": "Phone"}, validators=[DataRequired()])
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile"}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    monthly_contribution = FloatField('Monthly Contribution', render_kw={"placeholder": "Monthly Contribution"}, validators=[DataRequired()])
    date_joined = DateField('Date Joined', render_kw={"placeholder": "YYYY/MM/DD"}, validators=[DataRequired()])
    uuid = HiddenField('uuid')
    submit_member_add = SubmitField('Save Changes')
    submit_member_update = SubmitField('Save Changes')
    submit_member_delete = SubmitField('Delete')