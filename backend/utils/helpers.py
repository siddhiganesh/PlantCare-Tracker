import os
import uuid

from flask import current_app


def allowed_file(filename: str) -> bool:

    if "." not in filename:

        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in current_app.config[
        "ALLOWED_IMAGE_EXTENSIONS"
    ]


def save_image(file):

    if file is None:

        return None

    if file.filename == "":

        return None

    if not allowed_file(file.filename):

        return None

    extension = file.filename.rsplit(".", 1)[1].lower()

    filename = f"{uuid.uuid4().hex}.{extension}"

    upload_folder = current_app.config[
        "UPLOAD_FOLDER"
    ]

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    file.save(
        os.path.join(
            upload_folder,
            filename
        )
    )

    return filename


def delete_image(filename: str | None):

    if not filename:

        return

    path = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    if os.path.exists(path):

        os.remove(path)