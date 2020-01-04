from main import db
from datetime import datetime
import uuid

class Contribution(db.Model):
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    member_code = db.Column(db.String(20))
    period = db.Column(db.String(7)) # YYYY-MM
    amount = db.Column(db.Float)
    remarks = db.Column(db.String(50))