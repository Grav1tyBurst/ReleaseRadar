from models.artist import Artist
from clients.musicbrainz import get_releases


def main():
    artist = Artist("Her Bright Skies", 0)

    releases = get_releases(artist)

    print(f"Found {len(releases)} releases\n")

    for release in releases:
        print(
            f"{release.release_date} | "
            f"{release.release_type:<7} | "
            f"{release.title}"
        )

    print()
    print("Albums :", sum(r.release_type == "Album" for r in releases))
    print("EPs    :", sum(r.release_type == "EP" for r in releases))
    print("Singles:", sum(r.release_type == "Single" for r in releases))


if __name__ == "__main__":
    main()