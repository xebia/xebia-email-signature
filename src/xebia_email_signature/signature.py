import jinja2
import tidylib
import sys
import argparse


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
    output_text = template.render(data=contact_details)

    return output_text


def ask_details():
    """
    Ask for employee details

    Returns:
        dict: Employee details (full_name, email, phone, job_role,
                                linkedin_url)
    """
    contact_details = dict()

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

    validate_details(contact_details)

    sys.stdout = org_stdout

    return contact_details


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


def validate_html(raw_html):
    """
    Make sure we're producing valid HTML

    Returns:
        str: Verified HTML output
    """
    tidy_options = {
        "indent": "auto",
        "indent-spaces": 2,
        "wrap": 72,
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
        }
    else:
        employee_details = ask_details()

    rendered_output = render_template(employee_details, "signature.tpl")
    _ = validate_html(rendered_output)
    print(rendered_output)


if __name__ == "__main__":
    main()
