from setuptools import setup

setup(
    name="aio-lastfm",
    version="0.0.1",
    description="Python library for interacting with the Last.fm API asynchronously",
    long_description="Python library for interacting with the Last.fm API asynchronously",
    url="https://github.com/NachABR/aio-lastfm",
    author="NachABR",
    author_email="nachabr@protonmail.com",
    license="MIT",
    packages=["lastfm"],
    install_requires=[
        "aiohttp>=3.8",
        "asyncio",
    ],
)
