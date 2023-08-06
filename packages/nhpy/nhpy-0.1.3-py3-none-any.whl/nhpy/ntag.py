from enum import Enum

class NTag():
    class Types(Enum):
        ARTIST      = 1
        CATEGORY    = 2
        CHARACTER   = 3
        GROUP       = 4
        LANGUAGE    = 5
        PARODY      = 6
        TAG         = 7

    def __init__(self, id: int, name: str, type: Types, url: str, count: int):
        self._id = id
        self._type = type
        self._name = name
        self._url = url
        self._count = count

    @property
    def id(self) -> int:
        """Get id of Tag
        Retuns:
            int: id of Tag
        """

        return self._id

    @property
    def type(self) -> Types:
        """Get Type of Tag
        Retuns:
            Types: Type of Tag (e.g. language)
        """

        return self._type

    @property
    def name(self) -> str:
        """Get Name of Tag
        Retuns:
            str: Name of Tag (e.g. english)
        """

        return self._name

    @property
    def count(self) -> int:
        """Get Count of Tag
        Retuns:
            int: Count of how often used
        """

        return self._count
