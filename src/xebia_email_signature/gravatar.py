import hashlib
import logging
from functools import lru_cache
from io import BytesIO
from os import path
from typing import Optional

import numpy as np
import requests
from PIL import Image

_profile_mask = Image.open(
    path.join(path.dirname(__file__), "static", "profile-mask.png")
).convert("L")


@lru_cache
def load_profile_from_gravatar(email: str) -> Optional[Image.Image]:
    """
    returns profile picture associated with email on gravatar.com, or None if no picture was found.
    """
    if not email:
        return None

    size, _ = _profile_mask.size

    url = (
        "https://www.gravatar.com/avatar/"
        + hashlib.md5(email.lower().encode("utf8")).hexdigest()
    )

    response = requests.get(url, params={"size": size, "d": "404"})
    if response.status_code != 200:
        logging.warning(
            "no profile picture found for %s, %s",
            email,
            response.status_code,
        )
        return

    profile_picture = Image.open(BytesIO(response.content))

    # gravatar sometimes does not return the requested size
    if profile_picture.size != _profile_mask.size:
        profile_picture = profile_picture.resize(_profile_mask.size)
    return (
        profile_picture
        if profile_picture.mode == "RGB"
        else profile_picture.convert("RGB")
    )


def mask_profile_picture(profile_picture: Image) -> Image:
    """
    adds the profile picture in the shape of the _profile_mask
    """
    size = profile_picture.size
    if size != _profile_mask.size:
        profile_picture = profile_picture.resize(_profile_mask.size)

    rgb = np.array(profile_picture.convert("RGB"))
    opacity = np.array(_profile_mask)
    image_array = np.dstack((rgb, opacity))
    return Image.fromarray(image_array).resize(size=(150, 150))
