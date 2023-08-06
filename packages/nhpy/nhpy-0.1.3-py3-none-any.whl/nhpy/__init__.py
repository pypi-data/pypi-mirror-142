import requests
from typing import List
from .nbook import NBook, NTag, NImage, NPage
from .ncomment import NComment, NUser
from .api_paths import ApiPaths
from .__vars__ import __headers__

def from_json(data: dict) -> NBook:
    media_id = data["media_id"]
    normalise = {"j": "jpg", "p": "png"}
    normalise_ttypes = {
        "artist": NTag.Types.ARTIST,
        "category": NTag.Types.CATEGORY,
        "character": NTag.Types.CHARACTER,
        "group": NTag.Types.GROUP,
        "language": NTag.Types.LANGUAGE,
        "parody": NTag.Types.PARODY,
        "tag": NTag.Types.TAG,
    }
    lnpages = []
    tags = []

    # add Cover
    cover_type = normalise[data["images"]["cover"]["t"]]
    url = ApiPaths.book_cover(media_id, cover_type)
    cover = NImage(url, cover_type, data["images"]["cover"]["w"], data["images"]["cover"]["h"])

    # add Thumbnail
    cover_type = normalise[data["images"]["thumbnail"]["t"]]
    url = ApiPaths.book_cover(media_id, cover_type)
    thumbnail = NImage(url, cover_type, data["images"]["thumbnail"]["w"], data["images"]["thumbnail"]["h"])

    # Add all Pages
    for i in range(len(data["images"]["pages"])):
        cur_page = data["images"]["pages"][i]
        page_num = i + 1
        img_type = normalise[cur_page["t"]]

        url = ApiPaths.book_page(media_id, page_num, img_type)
        tmp_img = NImage(url, img_type, cur_page["w"], cur_page["h"])

        lnpages.append(NPage(page_num, tmp_img))

    # add tages
    for it in range(len(data["tags"])):
        cur_tag = data["tags"][it]
        tags.append(NTag(cur_tag["id"], cur_tag["name"], normalise_ttypes[cur_tag["type"]], cur_tag["url"], cur_tag["count"]))


    return NBook(data["id"], media_id, data["title"], data["upload_date"], tags, data["num_favorites"], lnpages, data["num_pages"], cover, thumbnail, data["scanlator"])


class NhPy:
    def __init__(self):
        pass

    def get_book(self, id: int) -> NBook:
        """Get Book By Id
        Args:
            id (int): Book Id

        Retuns:
            NBook
        """
        print(ApiPaths.host_url())
        err, data = self._make_request(ApiPaths.host_url() + f"/api/gallery/{str(id)}")
        if (err):
            return None

        return from_json(data)

    def get_related_books(self, id: int) -> list:
        """Get related Books
        Args:
            id (int): Book Id

        Retuns:
            list[NBook]
        """
        err, data = self._make_request(f"{ApiPaths.host_url()}/api/gallery/{str(id)}/related")
        if (err):
            return dict()

        ret_data = []

        for book in data["result"]:
            ret_data.append(from_json(book))

        return ret_data

    def search(self, query: list, page: int = 1) -> dict:
        """Search by query
        Args:
            query (list[str]): List of search tags (e.g. ["neko", "full-color"])

        Retuns:
            dict: Object with Search Reulsts (e.g. {"pages": 10, "per_page": 25, "books": list[NBook]})
        """
        err, data = self._make_request(f"{ApiPaths.host_url()}/api/galleries/search?query=" + "+".join(query) + "&page={page}")
        if (err):
            return None

        ret_data = {
            "pages": data["num_pages"],
            "per_page": data["per_page"],
            "books": []
        }

        for book in data["result"]:
            ret_data["books"].append(from_json(book))

        return ret_data

    def comments(self, id: int) -> list:
        """Get Comments from a Book
        Args:
            id (int): Book Id

        Retuns:
            list[NComment]: Comments of a Book
        """
        err, data = self._make_request(f"{ApiPaths.host_url()}/api/gallery/{id}/comments")
        if err:
            return None

        ret_data = []

        for comment in data:
            print(comment["poster"]["username"])
            tmp_user = NUser(comment["poster"]["id"], comment["poster"]["username"], comment["poster"]["slug"], comment["poster"]["is_superuser"], comment["poster"]["is_staff"])
            ret_data.append(NComment(comment["id"], comment["gallery_id"], tmp_user, ["post_date"], ["body"]))

        return ret_data


    def _make_request(self, url) -> list:
        response = requests.get(url, headers=__headers__)
        if (response.status_code != 200):
            return [True, dict()]

        return [False, response.json()]
