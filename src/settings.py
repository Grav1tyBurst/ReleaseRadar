import os
import yaml

from dotenv import load_dotenv

load_dotenv()

with open("config/config.yaml", "r", encoding="utf-8") as file:
    settings = yaml.safe_load(file)

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
LASTFM_USERNAME = os.getenv("LASTFM_USERNAME")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

LASTFM_PERIOD = settings["lastfm"]["period"]
LASTFM_FETCH_LIMIT = settings["lastfm"]["fetch_limit"]
LASTFM_MIN_PLAYCOUNT = settings["lastfm"]["min_playcount"]

