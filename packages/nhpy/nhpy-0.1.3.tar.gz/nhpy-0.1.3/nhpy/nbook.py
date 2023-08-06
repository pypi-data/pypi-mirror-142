from datetime import datetime
from typing import List
import json

from .npages import NPage, NImage
from .ntag import NTag
from .api_paths import ApiPaths

class NBook(object):
    def __init__(self, id: int, media_id: str, title: List[str], upload_date: int, tags: list[NTag], favs: int, pages: List[NPage], page_count: int, cover: NImage, thumbnail: NImage, scanlator: str):
        self._id            = id
        self._media_id      = media_id
        self._title         = title
        self._upload_date   = upload_date
        self._tags          = tags
        self._favs          = favs

        self._scanlator     = scanlator #currently unsed

        self._pages         = pages
        self._page_count    = page_count
        self._cover         = cover
        self._thumbnail     = thumbnail


    @property
    def id(self) -> int:
        """Get Book Id
        Returns:
            int: Book Id
        """
        return self._id

    @property
    def title(self) -> str:
        """Get all Book Titles
        Returns:
            list[str]: List of all Book Titles
        """
        return self._title

    def uploaded(self, raw: bool = False) -> int | str:
        """Get Upload Time of Book
        Args:
            raw (bool): If should be formated or raw UNIX Time Epoch should be retuned

        Returns:
            int|str: Formated Timestamp or raw UNIX Time Epoch
        """

        if raw == True:
            return datetime.utcfromtimestamp(self._upload_date).strftime("%d %b, %Y %H:%M:%S")

        return self._upload_date

    @property
    def tags(self) -> List[NTag]:
        """Get Tags of Book
        Returns:
            list[NTags]: List of Tags
        """

        return self._tags

    @property
    def fav_count(self) -> int:
        """Get how many People markt book as Favorite
        Returns:
            int: Favorites count
        """
        return self._favs

    @property
    def pages(self) -> List[NPage]:
        """Get all Pages of Book
        Returns:
            list[NPage]: Pages
        """
        return self._pages

    @property
    def page_count(self) -> int:
        """Get number of Pages
        Returns:
            int: Number of Pages
        """

        return self._page_count

    @property
    def cover(self) -> NImage:
        """Get Cover of Book
        Returns:
            NImage: Cover Image
        """

        return self._cover

    @property
    def thumbnail(self) -> NImage:
        """Get Thumbnail of Book
        Returns:
            NImage: Thumbnail Image
        """
        return self._thumbnail
