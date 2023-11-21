import os

from flask import Flask, request, render_template

from xebia_email_signature.inline_images import inline_images
from xebia_email_signature.signature import (
    get_theme,
    add_profile_picture,
    add_weekday_availability,
    add_formatted_phone,
    add_office_details,
)
from xebia_email_signature.new_signature import add_call_to_actions, \
    add_social_media, get_new_theme

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

@app.route("/new")
def generate_new_signature():
    return render_template("new_form.html")


@app.route("/new/signature", methods=["POST"])
def create_new_signature():
    is_https = request.is_secure
    data = add_formatted_phone(request.form)
    data = add_call_to_actions(data)
    data = add_social_media(data)

    jinjafile = "new_signature.html.jinja"
    response = render_template(jinjafile, data=data, theme=get_new_theme(data))
    return response


@app.route("/")
def generate_signature():
    return render_template("form.html")


@app.route("/signature", methods=["POST"])
def create_signature():
    try:
        data = add_profile_picture(
            request.form, (90, 90), request.files.get("profile_picture")
        )
    except ValueError as error:
        return error.args[0], 400

    data = add_office_details(data)
    data = add_weekday_availability(data)
    data = add_formatted_phone(data)

    jinjafile = (
        "signature.xpirit.html.jinja"
        if data["office"].__contains__("Xpirit")
        else "signature.html.jinja"
    )

    response = render_template(jinjafile, data=data, theme=get_theme(data))

    return (
        inline_images(response, request.url)
        if "on" == data.get("with_inline_images")
        else response
    )


def main():
    app.run(port=int(os.getenv("PORT", 8080)))


if __name__ == "__main__":
    main()
