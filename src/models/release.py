class Release:
    def __init__(
        self,
        mbid: str,
        artist: str,
        title: str,
        release_type: str,
        release_date: str,
        track_count: int | None = None,
        heard: bool = False,
    ):
        self.mbid = mbid
        self.artist = artist
        self.title = title
        self.release_type = release_type
        self.release_date = release_date
        self.track_count = track_count
        self.heard = heard