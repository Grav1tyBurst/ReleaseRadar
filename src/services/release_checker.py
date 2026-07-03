from services.artist_library import load_artists
from services.release_library import (
    load_releases,
    save_releases,
)

from services.release_sync import find_new_releases

from models.release import Release


def check_releases(
    limit: int | None = None,
) -> list[Release]:

    artists = load_artists()

    if limit is not None:
        artists = artists[:limit]

    known_releases = load_releases()

    all_releases = known_releases.copy()

    new_releases = []

    print(f"Checking {len(artists)} artists...\n")

    for artist in artists:

        print(f"Checking {artist.name}...")

        artist_new = find_new_releases(
            artist,
            all_releases,
        )

        new_releases.extend(artist_new)

        all_releases.extend(artist_new)

    save_releases(all_releases)

    return new_releases