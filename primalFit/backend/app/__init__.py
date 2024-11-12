from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize the database
    db.init_app(app)
    CORS(app)

    # Import and register routes
    with app.app_context():
        from . import routes, models  # Import models to register them with SQLAlchemy
        db.create_all()  # Create tables if they don't exist
        app.register_blueprint(routes.bp)

    return app
