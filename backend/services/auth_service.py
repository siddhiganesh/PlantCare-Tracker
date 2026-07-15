from flask_jwt_extended import create_access_token

from extensions import db
from models import User

from utils.security import (
    hash_password,
    verify_password
)

from utils.helpers import (
    save_image,
    delete_image
)


def register_user(username, email, password):

    username = username.strip()
    email = email.strip().lower()

    if User.query.filter_by(username=username).first():

        return {
            "success": False,
            "message": "Username already exists."
        }

    if User.query.filter_by(email=email).first():

        return {
            "success": False,
            "message": "Email already exists."
        }

    user = User(

        username=username,

        email=email,

        password=hash_password(password)

    )

    db.session.add(user)

    db.session.commit()

    return {
        "success": True,
        "message": "Registration successful."
    }


def login_user(email, password):

    email = email.strip().lower()

    user = User.query.filter_by(
        email=email
    ).first()

    if user is None:

        return {
            "success": False,
            "message": "Invalid email or password."
        }

    if not verify_password(
        password,
        user.password
    ):

        return {
            "success": False,
            "message": "Invalid email or password."
        }

    token = create_access_token(
        identity=str(user.id)
    )

    return {

        "success": True,

        "token": token,

        "user": {

            "id": user.id,

            "username": user.username,

            "email": user.email,

            "profileImage": user.profile_image,

            "createdAt": user.created_at.isoformat()

        }

    }


def get_profile(user_id):

    user = User.query.get(user_id)

    if user is None:

        return None

    total_reminders = 0
    completed_reminders = 0

    for plant in user.plants:

        total_reminders += len(
            plant.reminders
        )

        completed_reminders += len(
            [
                reminder
                for reminder in plant.reminders
                if reminder.completed
            ]
        )

    return {

        "id": user.id,

        "username": user.username,

        "email": user.email,

        "profileImage": user.profile_image,

        "createdAt": user.created_at.isoformat(),

        "totalPlants": len(user.plants),

        "totalReminders": total_reminders,

        "completedReminders": completed_reminders

    }


def update_profile_image(user_id, image):

    user = User.query.get(user_id)

    if user is None:

        return None

    if image is None:

        return None

    if user.profile_image:

        delete_image(user.profile_image)

    filename = save_image(image)

    user.profile_image = filename

    db.session.commit()

    return {

        "id": user.id,

        "username": user.username,

        "email": user.email,

        "profileImage": user.profile_image,

        "createdAt": user.created_at.isoformat(),

        "totalPlants": len(user.plants)

    }