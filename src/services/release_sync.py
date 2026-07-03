from models.artist import Artist
from models.release import Release

from clients.musicbrainz import get_releases


def find_new_releases(
    artist: Artist,
    known_releases: list[Release],
) -> list[Release]:

    current_releases = get_releases(artist)

    known_ids = {
        release.mbid
        for release in known_releases
    }

    new_releases = []

    for release in current_releases:
        if release.mbid not in known_ids:
            new_releases.append(release)

    return new_releases