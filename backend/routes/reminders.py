from flask import Blueprint

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from services.reminder_service import (
    get_all_reminders,
    get_reminder,
    complete_reminder,
    delete_reminder
)

reminders_bp = Blueprint(
    "reminders",
    __name__,
    url_prefix="/api/reminders"
)


@reminders_bp.route("", methods=["GET"])
@reminders_bp.route("/", methods=["GET"])
@jwt_required()
def reminders():

    user_id = int(
        get_jwt_identity()
    )

    return get_all_reminders(
        user_id
    ), 200


@reminders_bp.route("/<int:reminder_id>", methods=["GET"])
@jwt_required()
def reminder(reminder_id):

    user_id = int(
        get_jwt_identity()
    )

    reminder = get_reminder(
        user_id,
        reminder_id
    )

    if reminder is None:

        return {
            "message": "Reminder not found."
        }, 404

    return reminder, 200


# --------------------------------------------------------
# Manual reminder creation disabled
# --------------------------------------------------------

@reminders_bp.route("", methods=["POST"])
@reminders_bp.route("/", methods=["POST"])
@jwt_required()
def add_reminder():

    return {

        "message": "Reminders are generated automatically."

    }, 405


# --------------------------------------------------------
# Manual reminder editing disabled
# --------------------------------------------------------

@reminders_bp.route("/<int:reminder_id>", methods=["PUT"])
@jwt_required()
def edit_reminder(reminder_id):

    return {

        "message": "Automatic reminders cannot be edited."

    }, 405


# --------------------------------------------------------
# Mark reminder completed
# --------------------------------------------------------

@reminders_bp.route("/<int:reminder_id>", methods=["PATCH"])
@jwt_required()
def mark_completed(reminder_id):

    user_id = int(
        get_jwt_identity()
    )

    reminder = complete_reminder(

        user_id,

        reminder_id

    )

    if reminder is None:

        return {

            "message": "Reminder not found."

        }, 404

    return reminder, 200


# --------------------------------------------------------
# Delete reminder
# --------------------------------------------------------

@reminders_bp.route("/<int:reminder_id>", methods=["DELETE"])
@jwt_required()
def remove_reminder(reminder_id):

    user_id = int(
        get_jwt_identity()
    )

    success = delete_reminder(

        user_id,

        reminder_id

    )

    if not success:

        return {

            "message": "Reminder not found."

        }, 404

    return {

        "message": "Reminder deleted successfully."

    }, 200