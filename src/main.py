from providers.lastfm import get_artists


def main():
    print("ReleaseRadar\n")

    artists = get_artists()

    print(f"Found {len(artists)} artists\n")

    for artist in artists:
        print(f"{artist.name} ({artist.playcount} plays)")


if __name__ == "__main__":
    main()