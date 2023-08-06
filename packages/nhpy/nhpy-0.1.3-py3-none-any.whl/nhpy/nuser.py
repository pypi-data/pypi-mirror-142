class NUser:
    def __init__(self, id: int, username: str, slug: str, is_superuser: bool, is_staff: bool, favorite_tags: str = "", about: str = "", recent_favorites: list = []):
        self._id = id
        self._username = username
        self._slug = slug
        self._is_superuser = is_superuser
        self._is_staff = is_staff
        self._favorite_tags = favorite_tags
        self._about = about

        self._recent_favorites = recent_favorites

    @property
    def id(self) -> int:
        """Id of User
        """
        return self._id

    @property
    def username(self) -> str:
        """Username
        """
        return self._username

    @property
    def is_superuser(self) -> bool:
        """If User is Superuser
        """
        return self._is_superuser

    @property
    def is_staff(self) -> bool:
        """If User is Staff Member
        """
        return self._is_staff

    @property
    def favorite_tags(self) -> str:
        """Users Favorite Tags
        """
        return self._favorite_tags

    @property
    def about(self) -> str:
        """About Text
        """
        return self._about

    @property
    def recent_favorites(self) -> list:
        """Users recent Favorites
        """
        return self._recent_favorites
