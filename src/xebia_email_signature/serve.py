import os
from xebia_email_signature.inline_images import inline_images
from xebia_email_signature.signature import (
    add_office_details,
    get_color_scheme,
    add_profile_picture,
    add_weekday_availability,
)


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def generate_signature():
    return render_template("form.html")


@app.route("/signature", methods=["POST"])
def create_signature():
    data = add_office_details(request.form)
    data = add_weekday_availability(request.form)

    if data.get("profile_image_from_gravatar"):
        data = add_profile_picture(data)

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
