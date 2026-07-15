from dotenv import load_dotenv

load_dotenv()

import os

from flask import Flask
from flask import send_from_directory

from config import Config
from extensions import (
    db,
    cors,
    migrate,
    jwt
)

from routes.auth import auth_bp
from routes.plants import plants_bp
from routes.reminders import reminders_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(
        app,
        db
    )

    jwt.init_app(app)

    cors.init_app(
        app,
        resources={
            r"/api/*": {
                "origins": [
                    "http://localhost:5173",
                    "http://127.0.0.1:5173"
                ]
            }
        },
        supports_credentials=True
    )

    os.makedirs(
        app.config["UPLOAD_FOLDER"],
        exist_ok=True
    )

    app.register_blueprint(auth_bp)
    app.register_blueprint(plants_bp)
    app.register_blueprint(reminders_bp)

    @app.route("/")
    def home():

        return {
            "message": "Plant Care Tracker API is running."
        }

    @app.route("/uploads/<path:filename>")
    def uploaded_file(filename):

        return send_from_directory(
            app.config["UPLOAD_FOLDER"],
            filename
        )

    with app.app_context():

        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )