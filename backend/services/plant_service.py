from datetime import datetime, timedelta

from extensions import db
from models import (
    Plant,
    Reminder,
    WateringHistory
)

from utils.helpers import (
    save_image,
    delete_image
)


def serialize_plant(plant):

    next_watering = (
        plant.last_watered +
        timedelta(days=plant.watering_frequency)
    )

    return {

        "id": plant.id,

        "name": plant.name,

        "species": plant.species,

        "location": plant.location,

        "image": plant.image,

        "wateringFrequency": plant.watering_frequency,

        "sunlightRequirement": plant.sunlight_requirement,

        "lastWatered": plant.last_watered.isoformat(),

        "nextWatering": next_watering.isoformat(),

        "createdAt": plant.created_at.isoformat(),

        "userId": plant.user_id

    }


def get_all_plants(user_id):

    plants = Plant.query.filter_by(

        user_id=user_id

    ).order_by(

        Plant.created_at.desc()

    ).all()

    return [

        serialize_plant(plant)

        for plant in plants

    ]


def get_plant(user_id, plant_id):

    plant = Plant.query.filter_by(

        id=plant_id,

        user_id=user_id

    ).first()

    if plant is None:

        return None

    return serialize_plant(plant)


def create_plant(user_id, form, image):

    filename = save_image(image)

    plant = Plant(

        name=form.get("name"),

        species=form.get("species"),

        location=form.get("location"),

        watering_frequency=int(
            form.get("wateringFrequency")
        ),

        sunlight_requirement=form.get(
            "sunlightRequirement"
        ),

        last_watered=datetime.utcnow(),

        image=filename,

        user_id=user_id

    )

    db.session.add(plant)

    db.session.flush()

    reminder = Reminder(

        title=f"Water {plant.name}",

        reminder_date=(
            datetime.utcnow() +
            timedelta(
                days=plant.watering_frequency
            )
        ),

        completed=False,

        plant_id=plant.id

    )

    db.session.add(reminder)

    db.session.commit()

    return serialize_plant(plant)


def update_plant(

    user_id,

    plant_id,

    form,

    image

):

    plant = Plant.query.filter_by(

        id=plant_id,

        user_id=user_id

    ).first()

    if plant is None:

        return None

    plant.name = form.get("name")

    plant.species = form.get("species")

    plant.location = form.get("location")

    plant.watering_frequency = int(
        form.get("wateringFrequency")
    )

    plant.sunlight_requirement = form.get(
        "sunlightRequirement"
    )

    if image:

        delete_image(
            plant.image
        )

        plant.image = save_image(
            image
        )

    reminder = Reminder.query.filter_by(

        plant_id=plant.id,

        completed=False

    ).first()

    if reminder:

        reminder.title = f"Water {plant.name}"

        reminder.reminder_date = (

            plant.last_watered +

            timedelta(
                days=plant.watering_frequency
            )

        )

    db.session.commit()

    return serialize_plant(plant)


def water_plant(

    user_id,

    plant_id,

    notes=""

):

    plant = Plant.query.filter_by(

        id=plant_id,

        user_id=user_id

    ).first()

    if plant is None:

        return None

    now = datetime.utcnow()

    plant.last_watered = now

    history = WateringHistory(

        watered_on=now,

        notes=notes,

        plant_id=plant.id

    )

    db.session.add(history)

    reminders = Reminder.query.filter_by(

        plant_id=plant.id,

        completed=False

    ).all()

    for reminder in reminders:

        reminder.completed = True

    next_reminder = Reminder(

        title=f"Water {plant.name}",

        reminder_date=(

            now +

            timedelta(
                days=plant.watering_frequency
            )

        ),

        completed=False,

        plant_id=plant.id

    )

    db.session.add(next_reminder)

    db.session.commit()

    return serialize_plant(plant)


def delete_plant(

    user_id,

    plant_id

):

    plant = Plant.query.filter_by(

        id=plant_id,

        user_id=user_id

    ).first()

    if plant is None:

        return False

    if plant.image:

        delete_image(
            plant.image
        )

    db.session.delete(
        plant
    )

    db.session.commit()

    return True 