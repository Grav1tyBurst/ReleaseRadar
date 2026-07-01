import requests

from config import LASTFM_API_KEY, LASTFM_USERNAME
from models.artist import Artist

BASE_URL = "https://ws.audioscrobbler.com/2.0/"


def get_artists(limit=10):
    params = {
        "method": "user.gettopartists",
        "user": LASTFM_USERNAME,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "period": "12month",
        "limit": limit,
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    artists = []

    for artist in data["topartists"]["artist"]:
        artists.append(
            Artist(
                name=artist["name"],
                playcount=int(artist["playcount"])
            )
        )

    return artists