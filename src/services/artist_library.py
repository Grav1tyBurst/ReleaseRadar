from pathlib import Path
import yaml

from models.artist import Artist

DATA_DIR = Path("data")
ARTISTS_FILE = DATA_DIR / "artists.yaml"


def save_artists(artists: list[Artist]):
    DATA_DIR.mkdir(exist_ok=True)

    data = {
        "artists": [
            {
                "name": artist.name,
                "playcount": artist.playcount,
                "mbid": artist.mbid,
            }
            for artist in artists
        ]
    }

    with open(ARTISTS_FILE, "w", encoding="utf-8") as file:
        yaml.dump(
            data,
            file,
            allow_unicode=True,
            sort_keys=False
        )


def load_artists() -> list[Artist]:
    with open(ARTISTS_FILE, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    artists = []

    for artist in data["artists"]:
        artists.append(
            Artist(
                name=artist["name"],
                playcount=artist["playcount"],
                mbid=artist.get("mbid"),
            )
        )

    return artists