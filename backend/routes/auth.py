from flask import Blueprint
from flask import request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from services.auth_service import (
    register_user,
    login_user,
    get_profile,
    update_profile_image
)

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    result = register_user(

        username=data.get("username", ""),

        email=data.get("email", ""),

        password=data.get("password", "")

    )

    if result["success"]:

        return {

            "message": result["message"]

        }, 201

    return {

        "message": result["message"]

    }, 400


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    result = login_user(

        email=data.get("email", ""),

        password=data.get("password", "")

    )

    if not result["success"]:

        return {

            "message": result["message"]

        }, 401

    return {

        "token": result["token"],

        "user": result["user"]

    }, 200


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    profile = get_profile(

        int(get_jwt_identity())

    )

    if profile is None:

        return {

            "message": "User not found."

        }, 404

    return profile, 200


@auth_bp.route("/profile/image", methods=["PUT"])
@jwt_required()
def upload_profile_image():

    image = request.files.get("image")

    user = update_profile_image(

        int(get_jwt_identity()),

        image

    )

    if user is None:

        return {

            "message": "Image upload failed."

        }, 400

    return user, 200


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():

    return {

        "message": "Logged out successfully."

    }, 200