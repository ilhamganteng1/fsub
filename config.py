import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7552440587:AAFABzck-xRa70aCAwEw9XKECbfOFqHPRpc")
API_ID = int(os.environ.get("API_ID", "6"))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")


OWNER_ID = int(os.environ.get("OWNER_ID", "5839381774"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://iystampan:iystampan@iystore.yglf3jm.mongodb.net/?retryWrites=true&w=majority&appName=IYSTORE")
DB_NAME = os.environ.get("DB_NAME", "IYSTORE")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002298018816"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002270682191"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002496261674"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "60000000000")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[65839381774]
    for x in (os.environ.get("ADMINS", "65839381774").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")








CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "âŒDon't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Êœá´‡ÊŸÊŸá´</b> {mention}\n\n<b>á´€É´á´…á´€ Êœá´€Ê€á´œêœ± Ê™á´‡Ê€É¢á´€Ê™á´œÉ´É¢ á´…Éª á´„Êœá´€É´É´á´‡ÊŸ/É¢Ê€á´œá´˜ êœ±á´€Êá´€ á´œÉ´á´›á´œá´‹ á´á´‡É´á´É´á´›á´É´ á´ Éªá´…á´‡á´É´Êá´€ êœ±ÉªÊŸá´€á´‹á´€É´ á´Šá´ÉªÉ´ á´‹á´‡ á´„Êœá´€É´É´á´‡ÊŸ á´›á´‡Ê€ÊŸá´‡Ê™ÉªÊœ á´…á´€Êœá´œÊŸá´œ á´…ÉªÊ™á´€á´¡á´€Êœ ÉªÉ´Éª</b>\n\nð—”ð—¦ð—¨ð—£ð—”ð—¡ ð—šð—¥ð—”ð—§ð—œð—¦ : https://t.me/+H0a25vAVRik3MzE9")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)