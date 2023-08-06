## nhpy [![Downloads](https://pepy.tech/badge/nhpy)](https://pypi.org/project/nhpy/) ![](https://img.shields.io/pypi/format/nhpy) [![](https://img.shields.io/pypi/v/nhpy)](https://pypi.org/project/nhpy/) ![](https://img.shields.io/github/license/b3yc0d3/nhpy) ![](https://img.shields.io/github/languages/code-size/b3yc0d3/nhpy)
nehntai api wrapper for python.\
Read the [Documentation](https://github.com/b3yc0d3/nhpy/blob/main/DOCS/usage.md)

## Planning
- [X] get book by id
- [X] get related books
- [X] search with query
- [X] get comments of a book

#### user related
- [ ] login
- [ ] user search
- [ ] get user profile

## Code Snippet
```py
from nhpy import NhPy

nhpy = NhPy()

my_book = nhpy.get_book(394659)
rel_books = nhpy.get_related_books(my_book.id)
my_search = nhpy.search(["neko"])
book_comment = nhpy.comments(394659)

```
