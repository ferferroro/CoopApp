from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import html5

class CompanyMaintenanceForm(FlaskForm):
    company_name = StringField('Name', render_kw={"placeholder": "Name"}, validators=[DataRequired()])
    address = StringField('Address', render_kw={"placeholder": "Address"}, validators=[DataRequired()])
    phone = StringField('Phone', render_kw={"placeholder": "Phone"}, validators=[DataRequired()])
    mobile = StringField('Mobile', render_kw={"placeholder": "Mobile"}, validators=[DataRequired()])
    total_fund = FloatField('Total Fund',widget=html5.NumberInput(), render_kw={"placeholder": "Total Fund"}, validators=[DataRequired()])
    available_fund = FloatField('Available Fund',widget=html5.NumberInput(), render_kw={"placeholder": "Available Fund"}, validators=[DataRequired()])
    lended_fund = FloatField('Lended Fund',widget=html5.NumberInput(), render_kw={"placeholder": "Lended Fund"}, validators=[DataRequired()])
    total_profit = FloatField('Total Profit',widget=html5.NumberInput(), render_kw={"placeholder": "Total Profit"}, validators=[DataRequired()])
    interest_rate = FloatField('Interest Rate',widget=html5.NumberInput(), render_kw={"placeholder": "Interest Rate"}, validators=[DataRequired()])
    submit_company_update = SubmitField('Save')