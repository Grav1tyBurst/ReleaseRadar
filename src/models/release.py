class Release:
    def __init__(
        self,
        artist: str,
        title: str,
        release_type: str,
        release_date: str,
        track_count: int | None = None,
    ):
        self.artist = artist
        self.title = title
        self.release_type = release_type
        self.release_date = release_date
        self.track_count = track_count