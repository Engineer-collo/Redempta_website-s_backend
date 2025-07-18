from flask import Blueprint, request, jsonify
from extensions import db
from models import Subscribe
from sqlalchemy.exc import IntegrityError

subscribe_bp = Blueprint('subscribe', __name__)

@subscribe_bp.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        new_sub = Subscribe(email=email)
        db.session.add(new_sub)
        db.session.commit()
        return jsonify(new_sub.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already subscribed"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@subscribe_bp.route('/subscribe', methods=['GET'])
def list_subscriptions():
    subs = Subscribe.query.order_by(Subscribe.created_at.desc()).all()
    return jsonify([sub.to_dict() for sub in subs])
