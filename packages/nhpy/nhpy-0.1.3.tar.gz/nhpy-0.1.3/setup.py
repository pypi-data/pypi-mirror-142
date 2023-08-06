from setuptools import setup
from nhpy.__vars__ import __version__, __author__, __email__

with open('README.md', 'r') as rmdf:
    long_description = rmdf.read()

setup(
    name='nhpy',
    version=__version__,
    description='API wraper for nhentai.net',
    url="https://github.com/b3yc0d3/nhpy",
    author=__author__,
    author_email=__email__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['nhpy'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires = [
        "requests >= 2.27.1"
        # "beautifulsoup4 >= 4.10.0",
    ],
    project_urls={
        "Source": "https://github.com/b3yc0d3/nhpy",
        "Issue tracker": "https://github.com/b3yc0d3/nhpy/issues"
    }
)
