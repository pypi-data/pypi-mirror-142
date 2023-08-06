__version__tuple__ = ("0", "1", "0")
__author__ = ("b3yc0d3")
__email__ = ("b3yc0d3@dnmx.org")

__version__ = ".".join(__version__tuple__) # xx.xx.xx
__version_short__ = f"{__version__tuple__[0]}.{__version__tuple__[1]}" # xx.xx


# Variables
__base_url__ = "https://nhentai.net/"
__useragent__ = f"Mozilla/5.0 (compatible; nhpy/{__version__})"

__headers__ = {
    "User-Agent": __useragent__
}
