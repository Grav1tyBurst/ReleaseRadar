import requests

from settings import (
    LASTFM_API_KEY,
    LASTFM_USERNAME,
    LASTFM_PERIOD,
    LASTFM_FETCH_LIMIT,
    LASTFM_MIN_PLAYCOUNT,
)

from models.artist import Artist

BASE_URL = "https://ws.audioscrobbler.com/2.0/"


def get_artists():
    params = {
        "method": "user.gettopartists",
        "user": LASTFM_USERNAME,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "period": LASTFM_PERIOD,
        "limit": LASTFM_FETCH_LIMIT,
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    artists = []

    for artist in data["topartists"]["artist"]:
        playcount = int(artist["playcount"])

        if playcount < LASTFM_MIN_PLAYCOUNT:
            continue

        artists.append(
            Artist(
                name=artist["name"],
                playcount=playcount,
            )
        )

    return artists