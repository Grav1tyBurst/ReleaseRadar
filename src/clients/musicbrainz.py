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


def find_artist_id(artist: Artist) -> str | None:
    params = {
        "query": artist.name,
        "fmt": "json",
    }

    response = requests.get(
        BASE_URL + "artist",
        params=params,
        headers={
            "User-Agent": "ReleaseRadar/0.1"
        },
    )

    response.raise_for_status()

    data = response.json()

    if not data["artists"]:
        return None

    return data["artists"][0]["id"]


def get_releases(artist: Artist) -> list[Release]:
    artist_id = find_artist_id(artist)

    if artist_id is None:
        return []

    response = requests.get(
        BASE_URL + f"release-group?artist={artist_id}",
        params={
            "fmt": "json",
        },
        headers={
            "User-Agent": "ReleaseRadar/0.1"
        },
    )

    response.raise_for_status()

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