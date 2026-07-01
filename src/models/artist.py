from dataclasses import dataclass


@dataclass
class Artist:
    name: str
    playcount: int