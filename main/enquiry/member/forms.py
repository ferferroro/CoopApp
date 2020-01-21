from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class MemberEnquiryForm(FlaskForm):
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    first_name = StringField('Fist Name', render_kw={"placeholder": "Fist Name", "readonly": "readonly"})
    last_name = StringField('Last Name', render_kw={"placeholder": "Last Name", "readonly": "readonly"})
    address = StringField('Address', render_kw={"placeholder": "Address", "readonly": "readonly"})
    phone = StringField('Phone', render_kw={"placeholder": "Phone", "readonly": "readonly"})
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile", "readonly": "readonly"})
    email = StringField('Email', render_kw={"placeholder": "Email", "readonly": "readonly"})
    monthly_contribution = FloatField('Monthly Contribution', render_kw={"placeholder": "Monthly Contribution", "readonly": "readonly"})
    date_joined = DateField('Date Joined (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD", "readonly": "readonly"})
    enquiry_member_back= SubmitField('Back')