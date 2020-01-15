from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class SetupSequenceForm(FlaskForm):
    name = StringField('Name', render_kw={"placeholder": "Name"}, validators=[DataRequired()])
    prefix = StringField('Prefix', render_kw={"placeholder": "Prefix"}, validators=[DataRequired()])
    increment = IntegerField('Increment', render_kw={"placeholder": "Increment"}, validators=[DataRequired()])
    current = IntegerField('Current', render_kw={"placeholder": "Current"}, validators=[DataRequired()])
    uuid = HiddenField('uuid')
    submit_setup_sequence_add = SubmitField('Create')
    submit_setup_sequence_update = SubmitField('Update')
    submit_setup_sequence_delete = SubmitField('Delete')
    submit_setup_sequence_back = SubmitField('Back')