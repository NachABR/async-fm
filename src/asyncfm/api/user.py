from datetime import datetime
from typing import Optional

from lastfm import api
from lastfm.types import Album, APIResponse, Artist, Tag, Track, User
from lastfm.utils import get_images_


class LastFMUser:
    def __init__(self, api: "api.FM"):
        self.api = api

    async def get_info(self, username: str):
        params = {
            "method": "user.getinfo",
            "user": username,
        }
        data = await self.api._make_request(params=params)

        user_data = data["user"]
        return User(
            name=user_data["name"],
            age=user_data.get("age"),
            subscriber=user_data.get("subscriber"),
            realname=user_data.get("realname"),
            bootstrap=user_data.get("bootstrap"),
            playcount=user_data.get("playcount"),
            artist_count=user_data.get("artist_count"),
            playlists=user_data.get("playlists"),
            track_count=user_data.get("track_count"),
            album_count=user_data.get("album_count"),
            image=get_images_(user_data.get("image")),
            registered=datetime.fromtimestamp(int(user_data["registered"]["unixtime"])),
            country=user_data.get("country"),
            gender=user_data.get("gender"),
            url=user_data.get("url"),
            type=user_data.get("type"),
        )

    async def get_recent_tracks(
        self,
        username: str,
        limit: int = 5,
        page: int = 1,
        extended: bool = False,
        from_time: int = None,
        to_time: int = None,
    ) -> Optional["APIResponse"]:
        """
        Fetches the recent tracks of a Last.fm user.

        Args:
        username (str): The Last.fm username to fetch the recent tracks of.
        limit (int, optional): The number of results to fetch per page. Defaults to 50. Maximum is 200.
        page (int, optional): The page number to fetch. Defaults to first page.
        extended (bool, optional): Includes extended data in each artist, and whether or not the user has loved each track. Defaults to False.
        from_time (int, optional): Beginning timestamp of a range - only display scrobbles after this time, in UNIX timestamp format (integer number of seconds since 00:00:00, January 1st 1970 UTC). This must be in the UTC time zone.
        to_time (int, optional): End timestamp of a range - only display scrobbles before this time, in UNIX timestamp format (integer number of seconds since 00:00:00, January 1st 1970 UTC). This must be in the UTC time zone.

        Returns:
        Optional[APIResponse]: A list of Track objects representing the recent tracks, or None if there was an error.
        """
        params = {
            "method": "user.getrecenttracks",
            "user": username,
            "limit": limit,
            "page": page,
            "extended": 1 if extended else 0,
        }
        if from_time is not None:
            params["from"] = from_time
        if to_time is not None:
            params["to"] = to_time

        data = await self.api._make_request(params=params)

        if recent_tracks := data.get("recenttracks"):
            return APIResponse(
                data=list(
                    map(
                        lambda track: Track(
                            artist=track["artist"]["#text"],
                            title=track["name"],
                            album=track["album"]["#text"],
                            images=get_images_(track.get("image")),
                            now_playing="@attr" in track
                            and "nowplaying" in track["@attr"],
                        ),
                        recent_tracks["track"],
                    )
                ),
                total=recent_tracks.get("@attr", {}).get("total"),
            )
        return None

    async def get_top_artists(
        self,
        username: str,
        period: str = "overall",
        limit: int = 5,
        page: int = 1,
    ) -> Optional["APIResponse"]:
        """
        Fetches the top artists for a Last.fm user.

        Args:
        user (str): The Last.fm username to fetch top artists for.
        period (str, optional): The time period over which to retrieve top artists for. Defaults to "overall". Possible values are "overall", "7day", "1month", "3month", "6month", "12month".
        limit (int, optional): The number of results to fetch per page. Defaults to 50.
        page (int, optional): The page number to fetch. Defaults to first page.

        Returns:
        Optional["APIResponse"]: A list of Artist objects representing the top artists, or None if there was an error.
        """
        params = {
            "method": "user.gettopartists",
            "user": username,
            "period": period,
            "limit": limit,
            "page": page,
        }
        data = await self.api._make_request(params=params)
        if artists := data.get("topartists"):
            return APIResponse(
                data=list(
                    map(
                        lambda artist: Artist(
                            name=artist["name"],
                            images=get_images_(artist.get("image")),
                            playcount=artist["playcount"],
                            rank=artist["@attr"]["rank"],
                        ),
                        artists["artist"],
                    )
                ),
                total=artists.get("@attr").get("total"),
            )
        return None

    async def get_top_albums(
        self, username: str, period: str = "overall", limit: int = 5, page: int = 1
    ) -> Optional["APIResponse"]:
        """
        Fetches the top albums for a Last.fm user.

        Args:
            period (str, optional): The time period over which to retrieve top albums for. Defaults to "overall". Possible values are "overall", "7day", "1month", "3month", "6month", "12month".
            limit (int, optional): The number of results to fetch per page. Defaults to 50.
            page (int, optional): The page number to fetch. Defaults to first page.

        Returns:
            Optional[APIResponse]: A list of Album objects representing the top albums, or None if there was an error.
        """
        params = {
            "method": "user.gettopalbums",
            "user": username,
            "period": period,
            "limit": limit,
            "page": page,
        }
        data = await self.api._make_request(params=params)
        if albums := data.get("topalbums"):
            return APIResponse(
                data=list(
                    map(
                        lambda album: Album(
                            artist=album["artist"]["name"],
                            title=album["name"],
                            images=get_images_(album.get("image")),
                            playcount=album["playcount"],
                            rank=album["@attr"]["rank"],
                        ),
                        albums["album"],
                    )
                ),
                total=albums.get("@attr").get("total"),
            )
        return None

    async def get_top_tracks(
        self,
        username: str,
        period: str = "overall",
        limit: int = 5,
        page: int = 1,
    ) -> Optional["APIResponse"]:
        """
        Fetches the top tracks for a Last.fm user.

        Args:
        user (str): The Last.fm username to fetch top tracks for.
        period (str, optional): The time period over which to retrieve top tracks for. Defaults to "overall". Possible values are "overall", "7day", "1month", "3month", "6month", "12month".
        limit (int, optional): The number of results to fetch per page. Defaults to 50.
        page (int, optional): The page number to fetch. Defaults to first page.

        Returns:
        Optional["APIResponse"]: A list of Track objects representing the top tracks, or None if there was an error.
        """
        params = {
            "method": "user.gettoptracks",
            "user": username,
            "period": period,
            "limit": limit,
            "page": page,
        }

        data = await self.api._make_request(params=params)

        if top_tracks := data.get("toptracks"):
            return APIResponse(
                data=[
                    Track(
                        artist=track["artist"]["name"],
                        title=track["name"],
                        images=get_images_(track.get("image")),
                    )
                    for track in top_tracks["track"]
                ],
                total=top_tracks.get("@attr", {}).get("total"),
            )
        return None

    async def get_top_tags(
        self,
        username: str,
        limit: int = 5,
        page: int = 1,
    ) -> Optional["APIResponse"]:
        """
        Fetches the top tags for a Last.fm user.

        Args:
        user (str): The Last.fm username to fetch top tags for.
        limit (int, optional): The number of results to fetch per page. Defaults to 50.
        page (int, optional): The page number to fetch. Defaults to first page.

        Returns:
        Optional["APIResponse"]: A list of Artist objects representing the top tags, or None if there was an error.
        """
        params = {
            "method": "user.gettoptags",
            "user": username,
            "limit": limit,
            "page": page,
        }

        data = await self.api._make_request(params=params)

        if top_tags := data.get("toptags"):
            return APIResponse(
                data=[Tag(**tag) for tag in top_tags["tag"]],
                total=len(top_tags["tag"]),
            )
        return None

    async def get_weekly_artist_chart(
        self,
        username: str,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> Optional["APIResponse"]:
        """
        Get the Last.fm chart of top artists for a given week.

        Args:
            username (str): The Last.fm username to fetch the chart for.
            from_date (datetime.datetime, optional): The start date of the week.
            to_date (datetime.datetime, optional): The end date of the week.

        Returns:
            Optional[APIResponse]: A list of Artist objects representing the top artists, or None if there was an error.
        """
        params = {"method": "user.getweeklyartistchart", "user": username}
        if from_date is not None:
            params["from"] = from_date.strftime("%Y-%m-%d")
        if to_date is not None:
            params["to"] = to_date.strftime("%Y-%m-%d")

        data = await self.api._make_request(params=params)

        if weekly_chart := data.get("weeklyartistchart"):
            return APIResponse(
                data=list(
                    map(
                        lambda artist: Artist(
                            name=artist["name"],
                            playcount=artist["playcount"],
                            images=get_images_(images=images)
                            if (images := artist.get("image"))
                            else None,
                        ),
                        weekly_chart["artist"],
                    )
                ),
                total=len(weekly_chart["artist"]),
            )
        return None

    async def get_weekly_album_chart(
        self,
        username: str,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> Optional["APIResponse"]:
        """
        Get the Last.fm chart of top albums for a given week.

        Args:

        from_date (datetime.datetime, optional): The datetime for the beginning of the week.
        to_date (datetime.datetime, optional): The datetime for the end of the week.

        Returns:
        Optional[APIResponse]: A list of Album objects representing the top albums, or None if there was an error.
        """
        params = {
            "method": "user.getweeklyalbumchart",
            "user": username,
        }
        if from_date:
            params["from"] = from_date.strftime("%Y-%m-%d")
        if to_date:
            params["to"] = to_date.strftime("%Y-%m-%d")

        data = await self.api._make_request(params=params)

        if weekly_chart := data.get("weeklyalbumchart"):
            return APIResponse(
                data=list(
                    map(
                        lambda album: Album(
                            artist=album["artist"]["#text"],
                            title=album["name"],
                            images=get_images_(images=images)
                            if (images := album.get("image"))
                            else None,
                            rank=album["@attr"]["rank"],
                            playcount=album["playcount"],
                        ),
                        weekly_chart["album"],
                    )
                ),
                total=len(weekly_chart["album"]),
            )
        return None

    async def get_weekly_track_chart(
        self,
        username: str,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> Optional["APIResponse"]:
        """
        Fetches the weekly track chart for a Last.fm user.

        Args:
        username (str): The Last.fm username to fetch weekly track chart for.
        from_date (datetime.datetime): The date from which to start the weekly chart.
        to_date (datetime.datetime): The date to which to end the weekly chart.
        limit (int, optional): The number of results to fetch. Defaults to 50.

        Returns:
        Optional["APIResponse"]: A list of Track objects representing the weekly track chart, or None if there was an error.
        """
        params = {
            "method": "user.getweeklytrackchart",
            "user": username,
        }
        if from_date is not None:
            params["from"] = from_date.strftime("%Y-%m-%d")
        if to_date is not None:
            params["to"] = to_date.strftime("%Y-%m-%d")
        data = await self.api._make_request(params=params)

        if weekly_chart := data.get("weeklytrackchart"):
            return APIResponse(
                data=list(
                    map(
                        lambda track: Track(
                            artist=track["artist"]["#text"],
                            title=track["name"],
                            images=get_images_(track.get("image")),
                            rank=track["@attr"]["rank"],
                            playcount=track["playcount"],
                        ),
                        weekly_chart["track"],
                    )
                ),
                total=len(weekly_chart["track"]),
            )
        return None
