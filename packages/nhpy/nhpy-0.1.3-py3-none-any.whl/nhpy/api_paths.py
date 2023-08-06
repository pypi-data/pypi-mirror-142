import json
from typing import List

host = "https://nhentai.net"
host_images = ""
host_thumbnails = ""

class ApiPaths():

    @staticmethod
    def host_url() -> str:
        return "https://nhentai.net"

    @staticmethod
    def host_image_url() -> str:
        return "https://nhentai.net"

    @staticmethod
    def host_thumbnail_url() -> str:
        return "https://nhentai.net"

    @staticmethod
    def book_page(media_id: int, page_num: int, extension: str) -> str:
        return f"{host}/api/galleries/{media_id}/page_num.{extension}"

    @staticmethod
    def book_cover(media_id: int, extension: str) -> str:
        return f"{host}/api/galleries/{media_id}/cover.{extension}"
