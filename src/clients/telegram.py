from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from settings import TELEGRAM_BOT_TOKEN

from services.release_checker import check_releases
from services.message_formatter import (
    format_welcome,
    format_new_releases,
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        format_welcome()
    )


async def check(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    await update.message.reply_text(
        "Проверяю новые релизы..."
    )

    new_releases = check_releases(limit=5)

    await update.message.reply_text(
        format_new_releases(new_releases)
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

    print("Telegram bot is running...")

    application.run_polling()