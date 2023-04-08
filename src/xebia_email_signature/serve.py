import os
from io import BytesIO

from PIL import Image
from flask import Flask, request, render_template

from xebia_email_signature.gravatar import (
    load_profile_from_gravatar,
    mask_profile_picture,
)
from xebia_email_signature.inline_images import inline_images
from xebia_email_signature.signature import (
    get_color_scheme,
    add_profile_picture,
    add_weekday_availability,
    add_formatted_phone,
)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024


@app.route("/")
def generate_signature():
    return render_template("form.html")


@app.route("/signature", methods=["POST"])
def create_signature():
    image = None
    file = request.files.get("profile_picture")
    if file:
        if file.mimetype not in ["image/png", "image/jpeg", "image/jpg"]:
            return "only png and jpeg images allowed", 400

        if request.form.get("profile_image_from_gravatar"):
            return "either specify your own image or use gravatar.com", 400

        try:
            image = Image.open(BytesIO(file.stream.read()))
            image = mask_profile_picture(image)
        except Exception:
            return "failed to process uploaded image", 500

    elif request.form.get("profile_image_from_gravatar"):
        image = load_profile_from_gravatar(request.form.get("email"))
        if not image:
            return "no profile image found for email on gravatar.com", 400
        image = mask_profile_picture(image)

    data = add_profile_picture(request.form, image)
    data = add_weekday_availability(data)
    data = add_formatted_phone(data)

    response = render_template(
        "signature.html.jinja", data=data, color_scheme=get_color_scheme(data)
    )

    return (
        inline_images(response, request.url)
        if "on" == data.get("with_inline_images")
        else response
    )


def main():
    app.run(port=int(os.getenv("PORT", 8080)))


if __name__ == "__main__":
    main()
