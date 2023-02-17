## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQGuKwwAVUtsz-Bgmh5llCp4e5yMTEYRTGPy17gSUwu8I467-SekyWA8Beh479WHn2B4NkzFmvh625BNv8icXZb0qOkvsbhrjhfdz_nInAzCQCSq3vqHgkS4DhcT8sycwNb7G9GdNAqP18DX5Et570OaiA32Lvr9w7WuZu2P2sIuXlfujS19rkT78a3eAJEf7HBFDDAtdvoIQGR5kkQzshLTqU7aq4hkMFVh-1RWvpoz02-6uF2zLrLyRzbiVxDxt-ezJWvbLEyMvXQAk6dJOpVlxfPtKKAlxNFw4gd8Bdj2DzbCfbTPwXpr0bkqRicfX6SHkUDREF-PBIOOvaWcvqP497CKJAAAAAFkpMigAA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6197299374:AAFoIfkmDpMhqlT-yGTYEVSwpkI0C5L7pKg")
BOT_NAME = getenv("BOT_NAME", "❝𝐂𝐡𝐞𝐫𝐫𝐲 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭❞")

API_ID = int(getenv("API_ID", "28191500"))
API_HASH = getenv("API_HASH", "f7ec1f67ca70e86b01205740418317a9")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://zewdatabase:ijoXgdmQ0NCyg9DO@zewgame.urb3i.mongodb.net/ontap?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "D3AD_B0Y")
ALIVE_NAME = getenv("ALIVE_NAME", "❝𝐂𝐡𝐞𝐫𝐫𝐲 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭❞")
BOT_USERNAME = getenv("BOT_USERNAME", "Opmusix_bot")
OWNER_ID = getenv("OWNER_ID", "5567639956")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "lol")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ISHQ00_I")
6197299374:AAFoIfkmDpMhqlT-yGTYEVSwpkI0C5L7pKgUPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "YKD_I")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
