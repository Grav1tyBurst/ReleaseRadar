from services.artist_library import (
    save_artists,
)

from services.release_checker import (
    sync_releases,
)

from clients.lastfm import (
    get_artists,
)


def initialize_library():

    artists = get_artists()

    save_artists(artists)

    sync_releases()