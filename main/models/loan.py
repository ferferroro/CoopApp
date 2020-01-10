from main import db
from datetime import datetime
import uuid

class Loan(db.Model):
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    code = db.Column(db.String(20), unique=True)
    borrower_code = db.Column(db.String(20))
    type_loan =  db.Column(db.String(20)) # quote or loan
    date_loan = db.Column(db.DateTime, default=datetime.utcnow)
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    terms = db.Column(db.Integer)
    type_schedule =  db.Column(db.String(20)) # semi-montly or monthly
    is_approved = db.Column(db.Boolean) # disable edit of loan
    is_settled = db.Column(db.Boolean)
    amount = db.Column(db.Float)
    amount_gross = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    interest_amount = db.Column(db.Float)
    remarks = db.Column(db.String(50))