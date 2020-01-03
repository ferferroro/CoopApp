from main import db
from datetime import datetime
import uuid

class Borrower(db.Model):
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    mobile = db.Column(db.String(50))
    email = db.Column(db.String(50))
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    interest_rate = db.Column(db.Float)
    penalty_rate = db.Column(db.Float)
    balance = db.Column(db.Float)