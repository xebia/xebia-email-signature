import base64

import requests
from bs4 import BeautifulSoup


def inline_images(html_doc, base_url):
    soup = BeautifulSoup(html_doc, "html.parser")
    for image in soup.find_all("img"):
        url = image["src"]
        if url.startswith("data:"):
            continue
        if not url.startswith("http"):
            url = base_url + url
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"could not download {url}")
        data = base64.b64encode(response.content).decode("utf-8")
        image["src"] = "data:" + response.headers["content-type"] + ";base64," + data
    return str(soup)
