import base64

import requests
from datetime import datetime
from bs4 import BeautifulSoup
from functools import lru_cache


# the HTTP requests session cache
_session = requests.Session()


def get_content_of_url(url: str) -> (bytes, str):
    """
    returns the cached binary content and content type of the `url`.
    the content is cached for a maximum of 3600 seconds
    """
    @lru_cache(maxsize=128)
    def _get_content(url: str, expire_at: int):
        _ = expire_at  # only used to expire the cached result
        response = _session.get(url, headers={'User-Agent': 'curl/7.86.0'})
        if response.status_code != 200:
            raise ValueError(f"could not download {url}, {response.status_code}, {response.text}")
        return response.content, response.headers["content-type"]

    return _get_content(url, int(datetime.now().timestamp() / 3600 + 1))


def inline_images(html_doc: str, base_url: str):
    """
    replace all images references in the `html_doc` with an inline image representation.
    relative image references are suffixed to the `base_url`.

    >>> inline_images('<html><body><img src="https://xebia.com/wp-content/themes/xebia-theme/images/favicon.png"></body></html>', 'https://xebia.com')
    '<html><body><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAGmSURBVHgB7ZS7TsMwFIbPcUBClRAZkSqq8AQ0gJjpGzCyQDMiVKS+AeUNGApidEc2GJlgBiTCG1RcpI7hsjWNcdIWQUnqS4wY6D858Z98n2I7AJP892Ct5DWAsf2M+SCKsHL8TH3QyG7RKxPCLvnQTi0wPLCuX/yrNdtFfrmeUplBhM3VWffi5s3vgGF484k2rHhsWkIWHg+t4T1TEirwbwKyEssF9/T23Q/AAPyHgJSEBRsrBfd8VEIHniogkuA37VEJXfjgfdkZd0QZQLvXxQqxwNaFCwVkJLAP1oLHsUCQZDnmlha5a3l0bgCfAU24lEAi8Xp/liWRBy4toCShAI9DQCFTXdLg3z0YUwnCECgoRFqgPu85vWm+21nGhuvHtnhnh3dBMsJT8BXOd70j0x8e0ZMObYu6QgFVuKoEyQfHFke1Umf4MzLLgXngzUfqxaPawjbl19W0luhLYF74MLoSaAKeRwJNwXUl0CRcRwJNwz8lStU7TiuLJPA34HHqjmeHUfLnHCuBe8UtjyE6qSVCgqMHegiaSSTCqJ41HzHWhkn+Oh+a8VcshUdvFQAAAABJRU5ErkJggg=="/></body></html>'
    >>> inline_images('<html><body><img src="/wp-content/themes/xebia-theme/images/favicon.png"></body></html>', 'https://xebia.com')
    '<html><body><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAGmSURBVHgB7ZS7TsMwFIbPcUBClRAZkSqq8AQ0gJjpGzCyQDMiVKS+AeUNGApidEc2GJlgBiTCG1RcpI7hsjWNcdIWQUnqS4wY6D858Z98n2I7AJP892Ct5DWAsf2M+SCKsHL8TH3QyG7RKxPCLvnQTi0wPLCuX/yrNdtFfrmeUplBhM3VWffi5s3vgGF484k2rHhsWkIWHg+t4T1TEirwbwKyEssF9/T23Q/AAPyHgJSEBRsrBfd8VEIHniogkuA37VEJXfjgfdkZd0QZQLvXxQqxwNaFCwVkJLAP1oLHsUCQZDnmlha5a3l0bgCfAU24lEAi8Xp/liWRBy4toCShAI9DQCFTXdLg3z0YUwnCECgoRFqgPu85vWm+21nGhuvHtnhnh3dBMsJT8BXOd70j0x8e0ZMObYu6QgFVuKoEyQfHFke1Umf4MzLLgXngzUfqxaPawjbl19W0luhLYF74MLoSaAKeRwJNwXUl0CRcRwJNwz8lStU7TiuLJPA34HHqjmeHUfLnHCuBe8UtjyE6qSVCgqMHegiaSSTCqJ41HzHWhkn+Oh+a8VcshUdvFQAAAABJRU5ErkJggg=="/></body></html>'
    >>> inline_images('<html><body><img src="" alt="no image"></body></html>', 'https://xebia.com')
    '<html><body><img alt="no image" src=""/></body></html>'
    >>> inline_images('<html><body><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhE"/></body></html>', 'https://xebia.com')
    '<html><body><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhE"/></body></html>'
    """
    soup = BeautifulSoup(html_doc, "html.parser")
    for image in soup.find_all("img"):
        url = image["src"]
        if url.startswith("data:") or not url:
            continue
        if not url.startswith("http"):
            url = base_url + url
        content, content_type = get_content_of_url(url)
        data = base64.b64encode(content).decode("utf-8")
        image["src"] = "data:" + content_type + ";base64," + data
    return str(soup)
