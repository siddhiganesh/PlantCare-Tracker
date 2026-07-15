from flask import Blueprint

watering_bp = Blueprint(
    "watering",
    __name__,
    url_prefix="/api/watering"
)


@watering_bp.route("/", methods=["GET"])
def get_history():
    return {
        "message": "Get watering history"
    }, 200


@watering_bp.route("/", methods=["POST"])
def water_plant():
    return {
        "message": "Record watering"
    }, 201


@watering_bp.route("/<int:history_id>", methods=["DELETE"])
def delete_history(history_id):
    return {
        "message": f"Delete watering history {history_id}"
    }, 200