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
                "playcount": artist.playcount
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