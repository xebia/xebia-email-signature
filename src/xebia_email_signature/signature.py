import argparse
import base64
import sys
import re
from io import BytesIO
from typing import Optional
from copy import copy

import jinja2
import phonenumbers
import tidylib
from PIL import Image
from werkzeug.datastructures import FileStorage

from xebia_email_signature.gravatar import (
    load_profile_from_gravatar,
    mask_profile_picture,
)
from xebia_email_signature.inline_images import inline_images


def add_profile_picture(contact_details: dict, file: Optional[FileStorage]) -> dict:
    """
    add the profile picture of the user, base64 encoded
    """
    image: Image.Image = None
    result = {k: v for k, v in contact_details.items()}
    if file:
        if file.mimetype not in ["image/png", "image/jpeg", "image/jpg"]:
            raise ValueError("only png and jpeg images allowed")

        if contact_details.get("profile_image_from_gravatar"):
            raise ValueError("Either the profile image or use gravatar should be used")

        try:
            image = Image.open(BytesIO(file.stream.read()))
        except Exception:
            return "failed to process uploaded image", 500

        x, y = image.size
        if x != y:
            raise ValueError(f"profile image should be square, this one is {x}x{y}")
        image = mask_profile_picture(image)

    elif contact_details.get("profile_image_from_gravatar"):
        image = load_profile_from_gravatar(contact_details.get("email"))
        if not image:
            raise ValueError("no profile image found for email on gravatar.com")
        image = mask_profile_picture(image)
    else:
        # no image to add
        pass

    if image:
        buffer = BytesIO()
        image.save(buffer, format="png")
        result["profile_picture"] = base64.b64encode(buffer.getvalue()).decode("ascii")

    return result


def add_weekday_availability(contact_details: dict) -> dict:
    """
    adds the weekday_availability
    :param contact_details:
    :return:
    """
    result = {k: v for k, v in contact_details.items()}

    availability = [
        1 if contact_details.get("Mon") else 0,
        1 if contact_details.get("Tue") else 0,
        1 if contact_details.get("Wed") else 0,
        1 if contact_details.get("Thu") else 0,
        1 if contact_details.get("Fri") else 0,
        1 if contact_details.get("Sat") else 0,
        1 if contact_details.get("Sun") else 0,
    ]

    # make weekdays the default
    if all([v == 0 for v in availability]):
        availability = [1, 1, 1, 1, 1, 0, 0]

    value = _get_readable_weekdays(availability)
    timezone = contact_details.get("timezone", None)
    if timezone:
        value = f"{value} {timezone}"
    result["weekday_availability"] = value
    return result


def add_formatted_phone(contact_details: dict) -> dict:
    """
    adds the field formatted_phone to the contact details based
    on the phone field.
    >>> add_formatted_phone({'phone': '+31622374114'})
    {'phone': '+31622374114', 'formatted_phone': '+31 6 22374114'}
    >>> add_formatted_phone({})
    {}
    """
    result = {k: v for k, v in contact_details.items()}
    phone = contact_details.get("phone")
    if phone:
        result["formatted_phone"] = phonenumbers.format_number(
            phonenumbers.parse(phone),
            phonenumbers.PhoneNumberFormat.INTERNATIONAL,
        )
    return result


def _get_readable_weekdays(availability: [int]) -> str:
    """
    transforms an array of 7 weekday availability into a readable
    string.

    >>> _get_readable_weekdays([1,1,1,1,1])
    'Mon-Fri'
    >>> _get_readable_weekdays([1,1,0,1,1])
    'Mon-Tue, Thu-Fri'
    >>> _get_readable_weekdays([1,0,0,1,1])
    'Mon, Thu-Fri'
    """
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    available_days = []
    for i in range(len(availability)):
        if availability[i]:
            available_days.append(weekdays[i])

    if len(available_days) == 7:
        return "Every day"
    elif len(available_days) == 0:
        return "No days"
    elif len(available_days) == 1:
        return available_days[0]
    else:
        groups = []
        temp = [available_days[0]]
        for i in range(1, len(available_days)):
            if weekdays.index(available_days[i]) == weekdays.index(temp[-1]) + 1:
                temp.append(available_days[i])
            else:
                groups.append(temp)
                temp = [available_days[i]]
        groups.append(temp)
        result = ""
        for group in groups:
            if len(group) == 1:
                result += group[0] + ", "
            else:
                result += group[0] + "-" + group[-1] + ", "
        return result[:-2]


_themes = {
    "Xebia Academy": {
        "default": "#222222",
        "full_name": "#6C1D5F",
        "unit": "#5A5A5A",
        "link": "#06A99C",
        "logo_url": "https://cdn.xebia.com/assets/logos/academy.png",
        "url": "https://xebia.com/academy",
    },
    "default": {
        "default": "#222222",
        "full_name": "#6C1D5F",
        "unit": "#5A5A5A",
        "link": "#6C1D5F",
        "logo_url": "https://assets.oblcc.com/xebia/xebia.png",
        "url": "https://xebia.com",
    },
}


def get_theme(data: dict) -> dict:
    """
    returns the correct theme for the data['unit']. If data['dark_theme'] == "on",
    than all colors will be black.

    >>> get_theme({"unit": "Xebia Cloud", "dark_theme": "on"})
    {'default': 'black', 'full_name': 'black', 'unit': 'black', 'link': 'black', 'logo_url': 'https://assets.oblcc.com/xebia/xebia.png', 'url': 'https://xebia.com'}
    >>> get_theme({"unit": "Xebia Cloud", "dark_theme": "off"})
    {'default': '#222222', 'full_name': '#6C1D5F', 'unit': '#5A5A5A', 'link': '#6C1D5F', 'logo_url': 'https://assets.oblcc.com/xebia/xebia.png', 'url': 'https://xebia.com'}
    >>> get_theme({"unit": "Xebia Academy", "dark_theme": "on"})
    {'default': 'black', 'full_name': 'black', 'unit': 'black', 'link': 'black', 'logo_url': 'https://cdn.xebia.com/assets/logos/academy.png', 'url': 'https://xebia.com/training'}
    >>> get_theme({"unit": "Xebia Academy", "dark_theme": "off"})
    {'default': '#222222', 'full_name': '#6C1D5F', 'unit': '#5A5A5A', 'link': '#06A99C', 'logo_url': 'https://cdn.xebia.com/assets/logos/academy.png', 'url': 'https://xebia.com/training'}


    """
    result = copy(_themes.get(data.get("unit", "default"), _themes["default"]))
    if data.get("dark_theme", "off") == "on":
        for k, v in result.items():
            if re.match(r"^#[0-9A-Fa-f]{6}$", v):
                result[k] = "black"
    return result


def render_template(contact_details, template_name):
    """
    Load, render and return Jinja2 template

    Args:
        contact_details(dict): Contact details of the employee

    Returns:
        str: Rendered version of the template
    """
    template_loader = jinja2.PackageLoader(package_name="xebia_email_signature")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_name)
    output_text = template.render(
        data=contact_details, theme=get_theme(contact_details)
    )
    if "on" == contact_details.get("with_inline_images"):
        output_text = inline_images(output_text, "https://xebia.com")

    return output_text


def ask_details():
    """
    Ask for employee details

    Returns:
        dict: Employee details (full_name, email, phone, job_role,
                                linkedin_url)
    """
    contact_details = {}
    org_stdout = sys.stdout
    sys.stdout = sys.stderr

    print("To generate a signature, enter the following details...")

    full_name = input("full name (John Doe): ")
    contact_details.update({"full_name": full_name})

    email = input("e-mail (john.doe@xebia.com): ")
    contact_details.update({"email": email})

    phone = input("mobile phone (+31 6 12 34 56 78): ")
    contact_details.update({"phone": phone})

    job_role = input("job role (Cloud Consultant): ")
    contact_details.update({"job_role": job_role})

    unit = input("Unit: ")
    contact_details.update({"unit": unit})

    linkedin_url = input(
        "link to your LinkedIn profile (https://www.linkedin.com/in/johndoe/): "
    )
    contact_details.update({"linkedin_url": linkedin_url})

    github_url = input("link to your github account (https://github.com/johndoe): ")
    contact_details.update({"github_url": github_url})

    data = add_profile_picture(contact_details, None)
    data = add_weekday_availability(data)
    data = add_formatted_phone(data)
    validate_details(data)

    sys.stdout = org_stdout


def validate_details(contact_details):
    """
    Validate user input. Throw exception when not OK

    Returns:
        None
    """

    assert contact_details["full_name"]
    assert contact_details["email"]
    assert contact_details["phone"]
    assert contact_details["job_role"]
    assert contact_details["linkedin_url"]


def validate_html(raw_html) -> str:
    """
    Make sure we're producing valid HTML

    Returns:
        str: Verified HTML output
    """
    tidy_options = {
        "indent": "auto",
        "indent-spaces": 2,
        "wrap": 200,
        "markup": True,
        "output-xml": False,
        "input-xml": False,
        "show-warnings": True,
        "numeric-entities": True,
        "quote-marks": True,
        "quote-nbsp": True,
        "quote-ampersand": False,
        "break-before-br": False,
        "uppercase-tags": False,
        "uppercase-attributes": False,
        "doctype": "strict",
    }
    pretty_html_doc, errors = tidylib.tidy_document(raw_html, tidy_options)

    if errors:
        raise ValueError(f"Invalid HTML\n{errors}\n\n{raw_html}")

    return pretty_html_doc


def main():
    """
    Main function. Call only when script is invoked directly

    Returns:
        None
    """
    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        "-d", "--debug", help="Enable debug mode", action=argparse.BooleanOptionalAction
    )

    args = argParser.parse_args()
    if args.debug:
        employee_details = {
            "full_name": "John Doe <script>",
            "email": "john.doe@xebia.com",
            "phone": "+31 6 12 34 56 78",
            "job_role": "Consultant",
            "linkedin_url": "https://linkedin.com/user",
            "unit": "Xebia Cloud",
            "github_url": "https://github.com/user",
            "timezone": "Europe/Amsterdam",
        }
    else:
        employee_details = ask_details()

    employee_details = add_formatted_phone(employee_details)
    employee_details = add_weekday_availability(employee_details)
    rendered_output = render_template(employee_details, "signature.html.jinja")
    print(validate_html(rendered_output))


if __name__ == "__main__":
    main()
