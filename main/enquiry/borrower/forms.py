from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, BooleanField, HiddenField

class BorrowerEnquiryForm(FlaskForm):
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    first_name = StringField('Fist Name', render_kw={"placeholder": "Fist Name", "readonly": "readonly"})
    last_name = StringField('Last Name', render_kw={"placeholder": "Last Name", "readonly": "readonly"})
    address = StringField('Address', render_kw={"placeholder": "Address", "readonly": "readonly"})
    phone = StringField('Phone', render_kw={"placeholder": "Phone", "readonly": "readonly"})
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile", "readonly": "readonly"})
    email = StringField('Email', render_kw={"placeholder": "Email", "readonly": "readonly"})
    interest_rate = FloatField('Interest Rate', render_kw={"placeholder": "Interest Rate", "readonly": "readonly"})
    penalty_rate = FloatField('Pentalty Rate', render_kw={"placeholder": "Pentalty Rate", "readonly": "readonly"})
    balance = FloatField('Balance', render_kw={"placeholder": "Balance", "readonly": "readonly"})
    enquiry_borrower_back = SubmitField('Back')