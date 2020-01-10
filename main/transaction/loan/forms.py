from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, StringField, HiddenField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class TransactionLoanForm(FlaskForm):
    uuid = HiddenField('uuid')
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    borrower_code = StringField('Borrower Code', render_kw={"placeholder": "Borrower Code"}, validators=[DataRequired()])
    borrower_name = StringField('Name', render_kw={"placeholder": "Code", "readonly": "readonly"})
    date_start = DateField('Date Start (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"}, validators=[DataRequired()])
    date_end = DateField('Date End (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"})
    type_loan = SelectField('Loan Type', choices=[('',''), ('Quote','Quote'),('Loan','Loan')], validators=[DataRequired()])
    terms = IntegerField('Terms', render_kw={"placeholder": "Terms"}, validators=[DataRequired()])
    type_schedule = SelectField('Schedule Type', choices=[('',''), ('Semi-Monthly','Semi-Monthly'), ('Monthly','Monthly')], validators=[DataRequired()])
    is_settled = BooleanField('Is settled?')
    amount = FloatField('Amount', render_kw={"placeholder": "Amount"}, validators=[DataRequired()])
    amount_gross = FloatField('Gross', render_kw={"placeholder": "Gross"})
    interest_rate = FloatField('Interest rate', render_kw={"placeholder": "Interest rate"}, validators=[DataRequired()])
    interest_amount = FloatField('Interest amount', render_kw={"placeholder": "Interest amount"})
    remarks = StringField('Remarks', render_kw={"placeholder": "Remarks"}, validators=[DataRequired()])
    is_approved = BooleanField('Is Approved?')
    submit_transaction_loan_add = SubmitField('Save Changes')
    submit_transaction_loan_update = SubmitField('Save')
    submit_transaction_loan_delete = SubmitField('Delete')
    submit_transaction_loan_approve = SubmitField('Approve')

class TransactionLoanDetailForm(FlaskForm):
    uuid = HiddenField('uuid')
    loan_code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    type_line = StringField('Type Line', render_kw={"placeholder": "Type Line"}, validators=[DataRequired()])
    amount_to_pay = FloatField('Amount To Pay', render_kw={"placeholder": "Amount To Pay"}, validators=[DataRequired()])
    amount_payed = FloatField('Amount To Pay', render_kw={"placeholder": "Amount To Pay"}, validators=[DataRequired()])
    date_to_pay = DateField('Date To Pay (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"}, validators=[DataRequired()])
    date_payed = DateField('Date Payed (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"}, validators=[DataRequired()])
    submit_transaction_loan_detail_add = SubmitField('Save Changes')
    submit_transaction_loan_detail_update = SubmitField('Save')
    submit_transaction_loan_detail_delete = SubmitField('Delete')