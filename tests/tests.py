import asyncio
import datetime
import time
from src.asyncfm.api import LastFMAPI


def timeit(func):
    async def process(func, *args, **params):
        if asyncio.iscoroutinefunction(func):
            print('this function is a coroutine: {}'.format(func.__name__))
            return await func(*args, **params)
        else:
            print('this is not a coroutine')
            return func(*args, **params)

    async def helper(*args, **params):
        print('{}.time'.format(func.__name__))
        start = time.perf_counter()
        result = await process(func, *args, **params)

        # Test normal function route...
        # result = await process(lambda *a, **p: print(*a, **p), *args, **params)

        print(f"Time: {round(time.perf_counter() - start, 2)} mili/seconds")
        
        return result

    return helper


@timeit
async def main():
    fm = LastFMAPI(api_key="api_key")
    
    async with fm:
        test = "nachabr"
        user = await fm.user.get_info(username=test)
        print(user)
        recent = await fm.user.get_recent_tracks(username=test)
        print(recent)
        top_track = await fm.user.get_top_tracks(username=test)
        print(top_track)
        top_album = await fm.user.get_top_albums(username=test)
        print(top_album)
        top_artist = await fm.user.get_top_artists(username=test)
        print(top_artist)

        today = datetime.datetime.now().date()
        week = today - datetime.timedelta(weeks=1)

        await fm.user.get_weekly_album_chart(username=test, from_date=week, to_date=today)
        await fm.user.get_weekly_track_chart(username=test, from_date=today, to_date=week)
        await fm.user.get_weekly_artist_chart(username=test, from_date=week, to_date=today)
        await fm.user.get_top_tags(username=test)
    
    
asyncio.run(main())