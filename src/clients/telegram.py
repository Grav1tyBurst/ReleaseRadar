from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from settings import TELEGRAM_BOT_TOKEN

from services.release_checker import check_releases
from services.release_library import library_exists
from services.initialize import initialize_library

from services.message_formatter import (
    format_welcome,
    format_initialize,
    format_new_releases,
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    if library_exists():
        text = format_welcome()
    else:
        text = format_initialize()

    await update.message.reply_text(text)


async def check(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "Проверяю новые релизы..."
    )

    new_releases = check_releases()

    await update.message.reply_text(
        format_new_releases(new_releases)
    )

def progress_callback(
    current: int,
    total: int,
):
    print(f"{current}/{total}")

from clients.telegram import progress_callback
from services.artist_library import (
    save_artists,
)

from services.release_checker import (
    check_releases,
)

from clients.lastfm import (
    get_artists,
)


def initialize_library(
    progress_callback=progress_callback,
):

    artists = get_artists()

    save_artists(artists)

    check_releases(
        progress_callback=progress_callback,
    )

async def initialize(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "Импортирую библиотеку...\n"
        "Это может занять несколько минут."
    )

    initialize_library(progress_callback=progress_callback)

    await update.message.reply_text(
        "Импорт завершён."
    )


def run_bot():

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("check", check)
    )

    application.add_handler(
        CommandHandler("initialize", initialize)
    )

    print("Telegram bot is running...")

    application.run_polling()