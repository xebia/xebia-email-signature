import pkg_resources
import re
import json
from typing import Optional
from dataclasses import dataclass
import phonenumbers


@dataclass
class Office:
    address: str
    telephone: Optional[str]

    @property
    def address_lines(self) -> list[str]:
        return self.address.split("\n")

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


def get_office_by_name(name: str) -> Office:
    location = _offices.get(name, _offices["Hilversum, Netherlands"])
    return Office(address=location["address"], telephone=location.get("telephone", ""))


if __name__ == "__main__":
    print(get_office_by_name("Xebia"))
