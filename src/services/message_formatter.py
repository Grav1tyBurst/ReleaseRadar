from models.release import Release


def format_welcome() -> str:
    return (
        "🎵 ReleaseRadar\n\n"
        "Добро пожаловать!\n\n"
        "/check — Проверить новые релизы\n"
        "/unheard — Непрослушанные релизы\n"
        "/help — Справка"
    )


def format_initialize() -> str:
    return (
        "🎵 ReleaseRadar\n\n"
        "Добро пожаловать!\n\n"
        "Библиотека ещё не создана.\n\n"
        "/initialize — Импортировать исполнителей из Last.fm\n"
        "/help — Справка"
    )


def format_new_releases(
    releases: list[Release],
) -> str:

    if not releases:
        return "Новых релизов не найдено."

    lines = [
        f"Найдено новых релизов: {len(releases)}",
        "",
    ]

    for release in releases:
        lines.append(
            f"{release.artist}\n"
            f"{release.title}\n"
            f"{release.release_date}\n"
        )

    return "\n".join(lines)