from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from extensions import db, migrate
from routes import subscribe_bp
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configs
    database_url = os.getenv('DATABASE_URL', 'sqlite:///Social_media.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register blueprints
    app.register_blueprint(subscribe_bp, url_prefix="/api")

    # Test route
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "Hello from Flask application!"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)
