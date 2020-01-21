from main import db
import uuid
from datetime import datetime

class Member(db.Model):
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    code = db.Column(db.String(20), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    mobile = db.Column(db.String(50))
    email = db.Column(db.String(50))
    date_joined = db.Column(db.Date)
    monthly_contribution = db.Column(db.Float)
    search_tag = db.Column(db.String(100))
    created_by = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.String(20))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)