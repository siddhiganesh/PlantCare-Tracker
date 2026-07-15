from datetime import datetime

from extensions import db


# ==========================================================
# User Model
# ==========================================================

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    email = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    profile_image = db.Column(
        db.String(255),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    plants = db.relationship(
        "Plant",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy=True
    )

    def __repr__(self):
        return f"<User {self.username}>"


# ==========================================================
# Plant Model
# ==========================================================

class Plant(db.Model):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    species = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(100)
    )

    image = db.Column(
        db.String(255)
    )

    watering_frequency = db.Column(
        db.Integer,
        nullable=False
    )

    sunlight_requirement = db.Column(
        db.String(50)
    )

    last_watered = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        back_populates="plants"
    )

    reminders = db.relationship(
        "Reminder",
        back_populates="plant",
        cascade="all, delete-orphan",
        lazy=True
    )

    watering_history = db.relationship(
        "WateringHistory",
        back_populates="plant",
        cascade="all, delete-orphan",
        lazy=True
    )

    def __repr__(self):
        return f"<Plant {self.name}>"


# ==========================================================
# Reminder Model
# ==========================================================

class Reminder(db.Model):
    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(100),
        nullable=False
    )

    reminder_date = db.Column(
        db.DateTime,
        nullable=False
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    plant_id = db.Column(
        db.Integer,
        db.ForeignKey("plants.id"),
        nullable=False
    )

    plant = db.relationship(
        "Plant",
        back_populates="reminders"
    )

    def __repr__(self):
        return f"<Reminder {self.id}>"


# ==========================================================
# Watering History Model
# ==========================================================

class WateringHistory(db.Model):
    __tablename__ = "watering_history"

    id = db.Column(db.Integer, primary_key=True)

    watered_on = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    notes = db.Column(
        db.Text
    )

    plant_id = db.Column(
        db.Integer,
        db.ForeignKey("plants.id"),
        nullable=False
    )

    plant = db.relationship(
        "Plant",
        back_populates="watering_history"
    )

    def __repr__(self):
        return f"<WateringHistory {self.id}>"