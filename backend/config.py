import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

INSTANCE_DIR = os.path.join(
    BASE_DIR,
    "instance"
)

os.makedirs(
    INSTANCE_DIR,
    exist_ok=True
)


class Config:

    SECRET_KEY = "plant-care-secret"

    JWT_SECRET_KEY = "jwt-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(
            INSTANCE_DIR,
            "plantcare.db"
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "uploads"
    )

    ALLOWED_IMAGE_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "webp"
    }