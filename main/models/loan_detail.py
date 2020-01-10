from main import db
from datetime import datetime
import uuid

class LoanDetail(db.Model):
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    loan_code = db.Column(db.String(20))
    type_line = db.Column(db.String(20)) # amortization or penalty
    amount_to_pay = db.Column(db.Float)
    amount_payed = db.Column(db.Float)
    date_to_pay = db.Column(db.Date)
    date_payed = db.Column(db.Date)