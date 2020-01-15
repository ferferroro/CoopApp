from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class BorrowerMaintenanceForm(FlaskForm):
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    first_name = StringField('Fist Name', render_kw={"placeholder": "Fist Name"}, validators=[DataRequired()])
    last_name = StringField('Last Name', render_kw={"placeholder": "Last Name"}, validators=[DataRequired()])
    address = StringField('Address', render_kw={"placeholder": "Address"}, validators=[DataRequired()])
    phone = StringField('Phone', render_kw={"placeholder": "Phone"}, validators=[DataRequired()])
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile"}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    interest_rate = FloatField('Interest Rate', render_kw={"placeholder": "Interest Rate"}, validators=[DataRequired()])
    penalty_rate = FloatField('Pentalty Rate', render_kw={"placeholder": "Pentalty Rate"}, validators=[DataRequired()])
    balance = FloatField('Balance', render_kw={"placeholder": "Balance"}, validators=[DataRequired()])
    uuid = HiddenField('uuid')
    submit_borrower_add = SubmitField('Create')
    submit_borrower_update = SubmitField('Update')
    submit_borrower_delete = SubmitField('Delete')
    submit_borrower_back = SubmitField('Back')