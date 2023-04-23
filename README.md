# AsyncFM

Python library for interacting with the Last.fm API asynchronously.

## Installation

```bash
pip install async-fm
```

# Usage
First, you need to obtain an API key and secret from Last.fm. You can do this by creating an account on their [developer site](https://www.last.fm/api/account/create).


```python
import asyncio
import asyncfm

lastfm = asyncfm.LastFMAPI(api_key="api_key_here")


async def main():
    # Get the recent tracks for a user
    tracks = await lastfm.user.get_recent_tracks(username="rj")

    for track in tracks.data:
        print(f" ~ {track.artist} - {track.title}: image {track.images.extralarge}")
    print(f"Total: {tracks.total}")


asyncio.run(main())
```

## Requirements
- aiohttp
- pydantic

## Code Formatting
The code in this repository is formatted using [Black](https://github.com/psf/black). You can format the code in your local copy of the repository using:

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you encounter a bug or would like to make an improvement.

## Testing
We currently don't have any tests for this library, but we'd love your help in adding some! If you're interested in contributing, here's what you can do:

- Fork the repo
- Install the dependencies by running: `poetry install`.
- Write your tests in `tests` directory
- Run the tests with pytest
- Submit a pull request with your changes

Thanks for considering contributing tests to this library!

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for more information.