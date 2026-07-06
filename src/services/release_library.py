from pathlib import Path

import yaml

from models.release import Release

DATA_DIR = Path("data")
RELEASES_FILE = DATA_DIR / "releases.yaml"


def library_exists() -> bool:
    return RELEASES_FILE.exists()


def save_releases(releases: list[Release]):
    DATA_DIR.mkdir(exist_ok=True)

    data = {
        "releases": [
            {
                "mbid": release.mbid,
                "artist": release.artist,
                "title": release.title,
                "release_type": release.release_type,
                "release_date": release.release_date,
                "track_count": release.track_count,
            }
            for release in releases
        ]
    }

    with open(RELEASES_FILE, "w", encoding="utf-8") as file:
        yaml.dump(
            data,
            file,
            allow_unicode=True,
            sort_keys=False,
        )


def load_releases() -> list[Release]:
    if not RELEASES_FILE.exists():
        return []

    with open(RELEASES_FILE, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    releases = []

    for item in data.get("releases", []):
        releases.append(
            Release(
                mbid=item["mbid"],
                artist=item["artist"],
                title=item["title"],
                release_type=item["release_type"],
                release_date=item["release_date"],
                track_count=item["track_count"],
                heard=item.get("heard", False),
            )
        )

    return releases