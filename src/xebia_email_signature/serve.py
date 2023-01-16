import os
import phonenumbers
from xebia_email_signature.signature import add_office_details
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def generate_signature():
    return render_template("form.html")


@app.route("/signature", methods=["POST"])
def create_signature():
    data = add_office_details({k: v for k, v in request.form.items()})
    if data["type"] == "Unofficial signature":
        return render_template("simple-signature.html.jinja", data=data)
    else:
        return render_template("signature.html.jinja", data=data)


def main():
    app.run(port=int(os.getenv("PORT", 8080)))


if __name__ == "__main__":
    main()
