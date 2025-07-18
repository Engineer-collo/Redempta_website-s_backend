from app import app
from models import db, Subscribe
from datetime import datetime

def seed_subscriptions():
    emails = [
        "collins@example.com",
        "christine@example.com",
        "moringa_student@example.com",
        "techwriter@example.com",
        "user01@example.com"
    ]

    with app.app_context():
        print("🌱 Seeding subscriptions...")

        # Clear existing records
        db.session.query(Subscribe).delete()

        # Add new records
        for email in emails:
            subscription = Subscribe(email=email, created_at=datetime.utcnow())
            db.session.add(subscription)

        db.session.commit()
        print("✅ Done seeding subscriptions.")

if __name__ == "__main__":
    seed_subscriptions()
