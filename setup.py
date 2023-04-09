import pathlib
from setuptools import setup
from src.lastfm import __version__

long_description = pathlib.Path("./README.md").read_text()

setup(
    name="aio-lastfm",
    version=__version__,
    description="Python library for interacting with the Last.fm API asynchronously.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NachABR/aio-lastfm",
    download_url=f"https://github.com/NachABR/aio-lastfm/archive/refs/tags/v{__version__}.tar.gz",
    author="NachABR",
    author_email="nachabr@protonmail.com",
    license="MIT",
    packages=["lastfm"],
    install_requires=[
        "aiohttp>=3.8",
        "asyncio",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "last.fm",
        "lastfm",
        "Last.fm API",
        "asynchronous",
        "install_requires",
        "aiohttp",
        "asyncio",
        "MIT license",
        "GitHub",
    ],
)
