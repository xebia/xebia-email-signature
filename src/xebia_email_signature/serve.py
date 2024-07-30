import os
import json

from flask import Flask, request, render_template

from xebia_email_signature.inline_images import inline_images
from xebia_email_signature.signature_v1 import (
    get_theme,
    add_profile_picture,
    add_weekday_availability,
    add_formatted_phone,
    add_office_details,
)
from xebia_email_signature.signature import add_call_to_actions, \
    add_social_media, get_new_theme

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

def load_json_file(json_path):
    current_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_path, json_path)
    with open(path, 'r') as f:
        return json.load(f)

@app.after_request
def prepare_response(response):
    response.headers["Strict-Transport-Security"] = "max-age=2592000"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = "script-src 'self' https://www.googletagmanager.com 'sha384-9r5e85TmdjVjyjYzZAV3TG5A6tcrmD7JjNBGfT2r1wp9txUPttent/DMiMuOwRNG'; object-src 'none'"
    response.headers["Permissions-Policy"] = "clipboard-read=(self \"https://signature.xebia.com\"), clipboard-write=(self \"https://signature.xebia.com\")"
    response.headers["Referrer-Policy"] = "no-referrer-when-downgrade"
    response.headers["X-XSS-Protection"] = "1"
    return response

@app.route("/")
def generate_v2_signature():
    return render_template("form_v2.html")


@app.route("/v2/signature", methods=["POST"])
def create_v2_signature():
    data = add_formatted_phone(request.form)
    data = add_call_to_actions(data)
    data = add_social_media(data)
    data['scheme'] = request.headers.get('X-Forwarded-Proto', 'http')

    jinjafile = "signature.html.jinja"
    response = render_template(jinjafile, data=data, theme=get_new_theme(data))
    return response


@app.route("/v1")
def generate_v1_signature():
    return render_template("form_v1.html")


@app.route("/v1/signature", methods=["POST"])
def create_v1_signature():
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
        "signature_v1.xpirit.html.jinja"
        if data["office"].__contains__("Xpirit")
        else "signature_v1.html.jinja"
    )

    response = render_template(jinjafile, data=data, theme=get_theme(data))

    return (
        inline_images(response, request.url)
        if "on" == data.get("with_inline_images")
        else response
    )

@app.route("/v3")
def generate_v3_signature():
    return render_template("form_v3.html")


def main():
    app.run(port=int(os.getenv("PORT", 8080)))


if __name__ == "__main__":
    main()

@app.route("/v3/signature", methods=["POST"])
def create_v3_signature():
    current_path = os.path.abspath(os.path.dirname(__file__))
    
    data = add_formatted_phone(request.form)
    data = add_call_to_actions(data)
    data = add_social_media(data)
    data['scheme'] = request.headers.get('X-Forwarded-Proto', 'http')
    data['base64_images'] = load_json_file('static/base64-images.json')

    email_client = request.form.get("email_client")

    allowed_clients = [
        'outlook-mac',
        'outlook-new-mac',
        'outlook-win',
        'outlook-new-win',
        'native-win',
        'native-mac',
        'mobile-outlook-ios',
        'mobile-outlook-and',
        'mobile-native-ios'
    ]

    if email_client in allowed_clients:
        jinjafile = "signature-" + email_client + ".html.jinja"
    else:
        jinjafile = "wrong_client.html"

    if not os.path.exists(os.path.join(current_path, 'templates', jinjafile)):
        jinjafile = "signature.html.jinja"

    response = render_template(jinjafile, data=data, theme=get_new_theme(data))
    return response

@app.route("/v3/signature-eml", methods=["GET"])
def create_v3_signature_eml():
    data = add_formatted_phone(request.args)
    data = add_call_to_actions(data)
    data = add_social_media(data)
    data['scheme'] = request.headers.get('X-Forwarded-Proto', 'http')
    data['base64_images'] = load_json_file('static/base64-images.json')

    email_client = request.args.get("email_client")

    allowed_clients = [
        'native-mac'
    ]

    if email_client in allowed_clients:
        jinjafile = "signature-" + email_client + ".eml.jinja"
    else:
        jinjafile = "wrong_client.html"

    response = render_template(jinjafile, data=data, theme=get_new_theme(data))
    return response