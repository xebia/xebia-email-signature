import os
from xebia_email_signature.inline_images import inline_images
from xebia_email_signature.signature import add_office_details, get_color_scheme
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def generate_signature():
    return render_template("form.html")


@app.route("/signature", methods=["POST"])
def create_signature():
    data = add_office_details(request.form)
    if data["type"] == "Unofficial signature":
        response = render_template(
            "simple-signature.html.jinja",
            data=data,
            color_scheme=get_color_scheme(data),
        )
    else:
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
