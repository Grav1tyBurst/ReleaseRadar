class Artist:
    def __init__(
        self,
        name: str,
        playcount: int,
        mbid: str | None = None,
    ):
        self.name = name
        self.playcount = playcount
        self.mbid = mbid