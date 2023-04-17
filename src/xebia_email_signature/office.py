import pkg_resources
import json
from typing import Optional
from dataclasses import dataclass
import phonenumbers


@dataclass
class Office:
    address: str
    telephone: Optional[str]

    @property
    def telephone_formatted(self) -> str:
        return (
            phonenumbers.format_number(
                phonenumbers.parse(self.telephone),
                phonenumbers.PhoneNumberFormat.INTERNATIONAL,
            )
            if self.telephone
            else ""
        )


def load_locations():
    with pkg_resources.resource_stream(
        __name__, "/".join(("static", "offices.json"))
    ) as file:
        return json.load(file)


_offices = load_locations()


def get_office_by_name(name: str) -> dict:
    location = _offices.get(name, _offices["Xebia Netherlands"])
    return Office(address=location["address"], telephone=location.get("telephone", ""))


if __name__ == "__main__":
    print(get_office_by_name("Xebia"))
