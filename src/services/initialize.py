from services.artist_library import (
    save_artists,
)

from services.release_checker import (
    check_releases,
)

from clients.lastfm import (
    get_artists,
)


def initialize_library(
    progress_callback=None,
):

    artists = get_artists()

    save_artists(artists)

    check_releases(
        progress_callback=progress_callback,
    )