from clients.lastfm import get_artists
from services.artist_library import save_artists


def main():
    artists = get_artists()

    save_artists(artists)

    print(f"Saved {len(artists)} artists.")


if __name__ == "__main__":
    main()