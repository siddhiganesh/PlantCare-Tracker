from flask import Blueprint
from flask import request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from services.plant_service import (
    get_all_plants,
    get_plant,
    create_plant,
    update_plant,
    delete_plant,
    water_plant
)

plants_bp = Blueprint(
    "plants",
    __name__,
    url_prefix="/api/plants"
)


@plants_bp.route("", methods=["GET"])
@plants_bp.route("/", methods=["GET"])
@jwt_required()
def plants():

    user_id = int(
        get_jwt_identity()
    )

    return get_all_plants(
        user_id
    ), 200


@plants_bp.route("/<int:plant_id>", methods=["GET"])
@jwt_required()
def plant(plant_id):

    user_id = int(
        get_jwt_identity()
    )

    plant = get_plant(
        user_id,
        plant_id
    )

    if plant is None:

        return {
            "message": "Plant not found."
        }, 404

    return plant, 200


@plants_bp.route("", methods=["POST"])
@plants_bp.route("/", methods=["POST"])
@jwt_required()
def add_plant():

    user_id = int(
        get_jwt_identity()
    )

    plant = create_plant(

        user_id,

        request.form,

        request.files.get("image")

    )

    return plant, 201


@plants_bp.route("/<int:plant_id>", methods=["PUT"])
@jwt_required()
def edit_plant(plant_id):

    user_id = int(
        get_jwt_identity()
    )

    plant = update_plant(

        user_id,

        plant_id,

        request.form,

        request.files.get("image")

    )

    if plant is None:

        return {
            "message": "Plant not found."
        }, 404

    return plant, 200


@plants_bp.route("/<int:plant_id>/water", methods=["POST"])
@jwt_required()
def water(plant_id):

    user_id = int(
        get_jwt_identity()
    )

    data = request.get_json(silent=True) or {}

    plant = water_plant(

        user_id,

        plant_id,

        data.get(
            "notes",
            ""
        )

    )

    if plant is None:

        return {
            "message": "Plant not found."
        }, 404

    return plant, 200


@plants_bp.route("/<int:plant_id>", methods=["DELETE"])
@jwt_required()
def remove_plant(plant_id):

    user_id = int(
        get_jwt_identity()
    )

    success = delete_plant(

        user_id,

        plant_id

    )

    if not success:

        return {
            "message": "Plant not found."
        }, 404

    return {
        "message": "Plant deleted successfully."
    }, 200