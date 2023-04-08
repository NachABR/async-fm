import asyncio, timeit
import datetime
from lastfm.api import LastFMAPI

fm = LastFMAPI(api_key="972b6916be3c9598a8aae44b15fa3267")


async def main():
    test = "rj"
    await fm.user.get_info(username=test)
    await fm.user.get_recent_tracks(username=test)
    await fm.user.get_top_tracks(username=test)
    await fm.user.get_top_albums(username=test)
    await fm.user.get_top_artists(username=test)

    today = datetime.datetime.now().date()
    week = today - datetime.timedelta(weeks=1)

    await fm.user.get_weekly_album_chart(
        username=test, from_date=week, to_date=today
    )
    await fm.user.get_weekly_track_chart(
        username=test, from_date=today, to_date=week
    )
    await fm.user.get_weekly_artist_chart(
        username=test, from_date=week, to_date=today
    )
    await fm.user.get_top_tags(username=test)
    


time = timeit.timeit(lambda: asyncio.run(main()), number=10)
print(f"Tests passed. time: {round(time/10, 2)} seconds")