from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, BooleanField, HiddenField

class BorrowerEnquiryForm(FlaskForm):
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    first_name = StringField('Fist Name', render_kw={"placeholder": "Fist Name"})
    last_name = StringField('Last Name', render_kw={"placeholder": "Last Name"})
    address = StringField('Address', render_kw={"placeholder": "Address"})
    phone = StringField('Phone', render_kw={"placeholder": "Phone"})
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile"})
    email = StringField('Email', render_kw={"placeholder": "Email"})
    interest_rate = FloatField('Interest Rate', render_kw={"placeholder": "Interest Rate"})
    penalty_rate = FloatField('Pentalty Rate', render_kw={"placeholder": "Pentalty Rate"})
    balance = FloatField('Balance', render_kw={"placeholder": "Balance"})
    enquiry_borrower_back = SubmitField('Back')