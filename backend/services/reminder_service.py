from datetime import datetime, timedelta

from extensions import db
from models import (
    Reminder,
    Plant,
    WateringHistory
)


def serialize_reminder(reminder):

    return {

        "id": reminder.id,

        "plantId": reminder.plant_id,

        "plantName": reminder.plant.name,

        "title": reminder.title,

        "reminderDate": reminder.reminder_date.isoformat(),

        "completed": reminder.completed,

        "createdAt": reminder.created_at.isoformat()

    }


def get_all_reminders(user_id):

    reminders = (

        Reminder.query

        .join(Plant)

        .filter(

            Plant.user_id == user_id

        )

        .order_by(

            Reminder.completed.asc(),

            Reminder.reminder_date.asc()

        )

        .all()

    )

    return [

        serialize_reminder(reminder)

        for reminder in reminders

    ]


def get_reminder(user_id, reminder_id):

    reminder = (

        Reminder.query

        .join(Plant)

        .filter(

            Reminder.id == reminder_id,

            Plant.user_id == user_id

        )

        .first()

    )

    if reminder is None:

        return None

    return serialize_reminder(reminder)


# ----------------------------------------------------------
# Automatic reminder completion
# ----------------------------------------------------------

def complete_reminder(
    user_id,
    reminder_id
):

    reminder = (

        Reminder.query

        .join(Plant)

        .filter(

            Reminder.id == reminder_id,

            Plant.user_id == user_id

        )

        .first()

    )

    if reminder is None:

        return None

    reminder.completed = True

    reminder.plant.last_watered = datetime.utcnow()

    history = WateringHistory(

        plant_id=reminder.plant.id,

        watered_on=datetime.utcnow(),

        notes="Watered from reminder"

    )

    db.session.add(history)

    next_reminder = Reminder(

        plant_id=reminder.plant.id,

        title=f"Water {reminder.plant.name}",

        reminder_date=(

            datetime.utcnow()

            +

            timedelta(

                days=reminder.plant.watering_frequency

            )

        ),

        completed=False

    )

    db.session.add(next_reminder)

    db.session.commit()

    return serialize_reminder(

        next_reminder

    )


# ----------------------------------------------------------
# Read only
# ----------------------------------------------------------

def create_reminder(
    user_id,
    data
):

    return None


def update_reminder(
    user_id,
    reminder_id,
    data
):

    return None


def delete_reminder(
    user_id,
    reminder_id
):

    reminder = (

        Reminder.query

        .join(Plant)

        .filter(

            Reminder.id == reminder_id,

            Plant.user_id == user_id

        )

        .first()

    )

    if reminder is None:

        return False

    db.session.delete(

        reminder

    )

    db.session.commit()

    return True