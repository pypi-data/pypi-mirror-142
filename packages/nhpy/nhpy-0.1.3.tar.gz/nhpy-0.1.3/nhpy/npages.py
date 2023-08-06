class NImage():
    def __init__(self, url: str, type: str, width: int, height:int):
        """nhentai Book Image
        Args:
            url (str): url of image
            type (str): image type (e.g. png)
        """
        self._type      = type # png, jpg/jpeg
        self._url       = url
        self._width     = 0
        self._height    = 0
        self._raw       = b''

    @property
    def url(self) -> str:
        """URL of Image
        Returns:
            str: Image URL
        """
        return self._type

class NPage():
    def __init__(self, number: int, image: NImage):
        self._number = number
        self._image  = image

    @property
    def number(self) -> int:
        """Get Page Number
        Returns:
            int: Number of current Page
        """

        return self._number

    @property
    def image(self) -> NImage:
        """Get Image of Page
        Returns:
            NImage: Page Image
        """
        return self._image

class NPages():
    def __init__(self):
        self.pages = []
        self._num_pages = 0

    def get(self, page_num: int) -> NPage:
        if page_num > len(self.pages):
            return None

        return self.pages[page_num]

    @property
    def num_pages(self) -> int:
        """Get number of pages
        Returns:
            int: Number of pages
        """

        return self._num_pages
