from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class Image(BaseModel):
    small: str
    medium: str
    large: str
    extralarge: Optional[str] = None


class User(BaseModel):
    name: str
    age: Optional[str]
    subscriber: Optional[int]
    realname: str
    bootstrap: Optional[int]
    playcount: int
    artist_count: int
    playlists: int
    track_count: int
    album_count: int
    image: Optional[Image]
    registered: datetime
    country: str
    gender: str
    url: str
    type: str

    model_config = ConfigDict(populate_by_name=True)


class Track(BaseModel):
    artist: str
    title: str
    album: Optional[str] = None
    images: Optional[Image]
    now_playing: bool = False
    rank: Optional[int] = None
    playcount: Optional[int] = None


class Artist(BaseModel):
    name: str
    images: Optional[Image] = None
    playcount: int
    rank: Optional[int] = None


class Album(BaseModel):
    artist: str
    title: str
    images: Optional[Image]
    rank: Optional[int]
    playcount: int


class Tag(BaseModel):
    name: str
    count: int
    url: str


class Responses:
    class Tracks(BaseModel):
        tracks: List[Track]
        total: int

    class Artists(BaseModel):
        artists: List[Artist]
        total: int

    class Albums(BaseModel):
        albums: List[Album]
        total: int

    class Tags(BaseModel):
        tags: List[Tag]
        total: int
