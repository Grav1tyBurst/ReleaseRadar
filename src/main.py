from clients.telegram import run_bot
from services.release_library import get_unheard_releases

unheard = get_unheard_releases()

print(len(unheard))


def main():
    run_bot()


if __name__ == "__main__":
    main()