from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class MemberMaintenanceForm(FlaskForm):
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    first_name = StringField('Fist Name', render_kw={"placeholder": "Fist Name"}, validators=[DataRequired()])
    last_name = StringField('Last Name', render_kw={"placeholder": "Last Name"}, validators=[DataRequired()])
    address = StringField('Address', render_kw={"placeholder": "Address"}, validators=[DataRequired()])
    phone = StringField('Phone', render_kw={"placeholder": "Phone"}, validators=[DataRequired()])
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile"}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    monthly_contribution = FloatField('Monthly Contribution', render_kw={"placeholder": "Monthly Contribution"}, validators=[DataRequired()])
    date_joined = DateField('Date Joined (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"}, validators=[DataRequired()])
    uuid = HiddenField('uuid')
    submit_member_add = SubmitField('Create')
    submit_member_update = SubmitField('Update')
    submit_member_delete = SubmitField('Delete')
    submit_member_back= SubmitField('Back')