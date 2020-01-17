from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, StringField, HiddenField, BooleanField
from wtforms.validators import DataRequired

class TransactionContributionForm(FlaskForm):
    uuid = HiddenField('uuid')
    member_code = StringField('Member Code', render_kw={"placeholder": "Member Code"}, validators=[DataRequired()])
    period = StringField('Period', render_kw={"placeholder": "YYYY-MM"}, validators=[DataRequired()])
    amount = FloatField('Amount', render_kw={"placeholder": "Amount"}, validators=[DataRequired()])
    remarks = StringField('Remarks', render_kw={"placeholder": "Remarks"}, validators=[DataRequired()])
    is_approved = BooleanField('Is Approved?')
    submit_transaction_contribution_add = SubmitField('Create')
    submit_transaction_contribution_update = SubmitField('Update')
    submit_transaction_contribution_delete = SubmitField('Delete')
    submit_transaction_contribution_back = SubmitField('Back')
    submit_transaction_contribution_approve = SubmitField('Approve')