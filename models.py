from datetime import datetime
from sqlalchemy.orm import validates
from extensions import db

class Subscribe(db.Model):
    __tablename__ = 'subscribes'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @validates('email')
    def validate_email(self, key, email):
        if not email or "@" not in email:
            raise ValueError("Invalid email address")
        return email

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self):
        return f"<Subscribe id={self.id} email={self.email}>"
