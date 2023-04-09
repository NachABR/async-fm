import pathlib
from setuptools import setup, find_packages

long_description = pathlib.Path("./README.md").read_text()

setup(
    name="aio-lastfm",
    version="0.0.1",
    description="Python library for interacting with the Last.fm API asynchronously.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NachABR/aio-lastfm",
    download_url="https://github.com/NachABR/aio-lastfm/archive/refs/tags/v0.0.1.tar.gz",
    author="NachABR",
    author_email="nachabr@protonmail.com",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
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
