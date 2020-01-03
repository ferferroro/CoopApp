from main import db
from flask_login import UserMixin
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(200))
    display_name = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def hash_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return (self.uuid)