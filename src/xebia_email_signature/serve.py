import os
from copy import deepcopy
import phonenumbers
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def generate_signature():
    return render_template("form.html")


@app.route("/signature", methods=["POST"])
def create_signature():
    data = {k: v for k, v in request.form.items()}
    if "phone" in data:
        data["phone"] = phonenumbers.format_number(
            phonenumbers.parse(data["phone"]),
            phonenumbers.PhoneNumberFormat.INTERNATIONAL,
        )
    if data["type"] == "Unofficial signature":
        return render_template("simple-signature.tpl", data=data)
    else:
        return render_template("signature.tpl", data=data)


def main():
    app.run(port=int(os.getenv("PORT", 8080)))


if __name__ == "__main__":
    main()
