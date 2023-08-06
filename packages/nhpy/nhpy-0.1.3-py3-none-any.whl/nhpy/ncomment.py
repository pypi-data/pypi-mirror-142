from .nuser import NUser

class NComment:
    def __init__(self, id: int, gallery_id: int, author: NUser, post_date: int, body: str):
        self._id         = id
        self._gallery_id = gallery_id
        self._author     = author
        self._post_date  = post_date
        self._body       = body

    @property
    def id(self) -> int:
        """Comment Id
        """
        return self._id

    @property
    def gallery_id(self) -> int:
        """Id of Book
        """
        return self._gallery_id

    @property
    def author(self) -> NUser:
        """Comment Author
        """
        return self._author

    @property
    def post_date(self) -> int:
        """Timestamp when Comment was Posted
        """
        return self._post_date

    @property
    def body(self) -> str:
        """Comment Body
        """
        return self._body
