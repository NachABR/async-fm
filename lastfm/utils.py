from typing import List, Dict
from lastfm.types import Image

# internt utility
def get_images_(images: List[Dict]):
    return Image(**{size["size"]: size["#text"] for size in images if size.get("size")})
