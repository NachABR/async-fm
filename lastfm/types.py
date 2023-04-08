from datetime import datetime
from typing import Optional, List, Union
from pydantic import BaseModel


class Image(BaseModel):
    small: str
    medium: str
    large: str
    extralarge: Optional[str]


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

    class Config:
        allow_population_by_field_name = True


class Track(BaseModel):
    artist: str
    title: str
    album: Optional[str]
    images: Optional[Image]
    now_playing: bool = False
    rank: Optional[int]
    playcount: Optional[int]


class Artist(BaseModel):
    name: str
    images: Optional[Image]
    playcount: int
    rank: Optional[int]


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


class APIResponse(BaseModel):
    data: Optional[List[Union["Album", "Artist", "Track", "Tag"]]]
    total: int
