import time
import requests

from models.artist import Artist
from models.release import Release

BASE_URL = "https://musicbrainz.org/ws/2/"

ALLOWED_TYPES = {
    "Album",
    "EP",
    "Single",
}

BLOCKED_SECONDARY_TYPES = {
    "Live",
    "Compilation",
    "Remix",
    "Demo",
}


def musicbrainz_request(
    endpoint: str,
    params: dict,
):
    time.sleep(1)

    response = requests.get(
        BASE_URL + endpoint,
        params=params,
        headers={
            "User-Agent": "ReleaseRadar/0.1"
        },
        timeout=30,
    )

    response.raise_for_status()

    return response


def find_artist_id(artist: Artist) -> str | None:
    # Если MBID уже известен — используем его
    if artist.mbid:
        return artist.mbid

    params = {
        "query": artist.name,
        "fmt": "json",
    }

    response = musicbrainz_request(
        "artist",
        params,
    )

    data = response.json()

    if not data["artists"]:
        return None

    artist.mbid = data["artists"][0]["id"]

    return artist.mbid


def get_releases(artist: Artist) -> list[Release]:
    artist_id = find_artist_id(artist)

    if artist_id is None:
        return []

    response = musicbrainz_request(
        "release-group",
        {
            "artist": artist_id,
            "fmt": "json",
        },
    )

    data = response.json()

    releases = []

    for item in data["release-groups"]:

        primary_type = item.get("primary-type")
        secondary_types = item.get("secondary-types", [])

        if primary_type not in ALLOWED_TYPES:
            continue

        if any(t in BLOCKED_SECONDARY_TYPES for t in secondary_types):
            continue

        releases.append(
            Release(
                mbid=item["id"],
                artist=artist.name,
                title=item.get("title", "Unknown"),
                release_type=primary_type,
                release_date=item.get("first-release-date", ""),
                track_count=None,
            )
        )

    releases.sort(key=lambda release: release.release_date)

    return releases


def get_latest_release(artist: Artist) -> Release | None:
    return None