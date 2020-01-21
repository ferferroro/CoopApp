from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, StringField, HiddenField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import html5
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError

class TransactionLoanForm(FlaskForm):
    uuid = HiddenField('uuid')
    code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    borrower_code = StringField('Borrower Code', render_kw={"placeholder": "Borrower Code"}, validators=[DataRequired()])
    borrower_name = StringField('Name', render_kw={"placeholder": "Code", "readonly": "readonly"})
    date_start = DateField('Date Start', format='%Y-%m-%d', render_kw={"onkeydown": "return false"}, validators=[DataRequired()])
    date_end = DateField('Date End (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"})
    type_loan = SelectField('Loan Type', choices=[('',''), ('Quote','Quote'),('Loan','Loan')], validators=[DataRequired()])
    terms = IntegerField('Terms', widget=html5.NumberInput(), render_kw={"placeholder": "Terms"}, validators=[DataRequired()])
    type_schedule = SelectField('Schedule Type', choices=[('',''), ('Semi-Monthly','Semi-Monthly'), ('Monthly','Monthly')], validators=[DataRequired()])
    is_settled = BooleanField('Is settled?')
    amount = FloatField('Amount', widget=html5.NumberInput(), render_kw={"placeholder": "Amount"}, validators=[DataRequired()])
    amount_gross = FloatField('Gross', render_kw={"placeholder": "Gross"})
    interest_rate = FloatField('Interest rate', widget=html5.NumberInput(), render_kw={"placeholder": "Interest rate"}, validators=[DataRequired()])
    interest_amount = FloatField('Interest amount', render_kw={"placeholder": "Interest amount"})
    remarks = StringField('Remarks', render_kw={"placeholder": "Remarks"}, validators=[DataRequired()])
    is_approved = BooleanField('Is Approved?')
    submit_transaction_loan_add = SubmitField('Create')
    submit_transaction_loan_update = SubmitField('Update')
    submit_transaction_loan_delete = SubmitField('Delete')
    submit_transaction_loan_approve = SubmitField('Approve')
    submit_transaction_loan_penalty_add = SubmitField('Add Penalty')
    submit_transaction_loan_settle = SubmitField('Complete')
    submit_transaction_loan_back = SubmitField('Back')

    def validate_terms(form, field):
        if int(field.data) < 1:
            raise ValidationError("This field is required.")
        else:
            if form.type_schedule.data == 'Semi-Monthly' and int(field.data) > 24:
                raise ValidationError("Maximum Terms is 1 year")
            if form.type_schedule.data == 'Monthly' and int(field.data) > 12:
                raise ValidationError("Maximum Terms is 1 year")

class TransactionLoanDetailForm(FlaskForm):
    uuid = HiddenField('uuid')
    loan_code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    type_line = StringField('Type Line', render_kw={"placeholder": "Type Line"})
    amount_to_pay = FloatField('Amount To Pay', render_kw={"placeholder": "0.00"})
    amount_payed = FloatField('Enter Payment', render_kw={"placeholder": "0.00"}, validators=[DataRequired()])
    date_to_pay = DateField('Due (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"})
    date_payed = DateField('Date Payed (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"})
    term = IntegerField('Term', render_kw={"placeholder": "Term", "readonly": "readonly"})
    amount_base = FloatField('Principal', render_kw={"placeholder": "0.00"})
    amount_interest = FloatField('Interest', render_kw={"placeholder": "0.00"})
    submit_transaction_loan_detail_cancel = SubmitField('Close', render_kw={"data-dismiss": "modal"})
    submit_transaction_loan_detail_pay = SubmitField('Pay')


class TransactionLoanDetailPenaltyForm(FlaskForm):
    uuid = HiddenField('uuid')
    loan_code = HiddenField('loan_code')
    # loan_code = StringField('Code', render_kw={"placeholder": "Code", "readonly": "readonly"})
    type_line = StringField('Type Line', render_kw={"placeholder": "Type Line"})
    amount_to_pay = FloatField('Amount To Pay', render_kw={"placeholder": "0.00"})
    amount_payed = FloatField('Enter Payment', render_kw={"placeholder": "0.00"}, validators=[DataRequired()])
    date_to_pay = DateField('Due (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"})
    date_payed = DateField('Date Payed (YYYY-MM-DD)', render_kw={"placeholder": "YYYY-MM-DD"})
    term = IntegerField('Term', render_kw={"placeholder": "Term", "readonly": "readonly"})
    amount_base = FloatField('Principal', render_kw={"placeholder": "0.00"})
    amount_interest = FloatField('Interest', render_kw={"placeholder": "0.00"})

    submit_transaction_loan_detail_penalty_cancel = SubmitField('Close', render_kw={"data-dismiss": "modal"})
    submit_transaction_loan_detail_penalty_submit = SubmitField('Add')