import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv

load_dotenv("config.env")


logging.basicConfig(level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger("fsub")

# Bot token dari @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_DB = int(os.environ.get("CHANNEL_DB", ""))

ADMINS = [int(i) for i in os.environ.get("ADMINS").split()]

# Protect Content
PROTECT_CONTENT = eval(os.environ.get("PROTECT_CONTENT", "True"))

# Database
DATABASE_NAME = BOT_TOKEN.split(":", 1)[0]
DATABASE_URL  = os.environ.get("DB_URI", "")

FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", ""))
FORCE_SUB_TOTAL = 1
FORCE_SUB_      = {}
while True:
    key   = f"FORCE_SUB_{FORCE_SUB_TOTAL}"
    value = os.environ.get(key)
    if value is None:
        break
    FORCE_SUB_[FORCE_SUB_TOTAL] = int(value)
    FORCE_SUB_TOTAL += 1

