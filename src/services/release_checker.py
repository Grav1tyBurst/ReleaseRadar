from services.artist_library import load_artists
from services.release_library import (
    load_releases,
    save_releases,
)
from services.release_sync import find_new_releases
from services.progress_reporter import ProgressReporter

from models.release import Release


def check_releases(
    limit: int | None = None,
    reporter: ProgressReporter | None = None,
) -> list[Release]:

    artists = load_artists()

    if limit is not None:
        artists = artists[:limit]

    known_releases = load_releases()

    all_releases = known_releases.copy()

    new_releases = []

    print(f"Checking {len(artists)} artists...\n")

    total = len(artists)

    for index, artist in enumerate(
        artists,
        start=1,
    ):

        print(f"Checking {artist.name}...")

        artist_new = find_new_releases(
            artist,
            all_releases,
        )

        new_releases.extend(artist_new)

        all_releases.extend(artist_new)

        if reporter:
            reporter.report(
                index,
                total,
            )

    save_releases(all_releases)

    return new_releases