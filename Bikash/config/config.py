import os
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
  load_dotenv("Internal")

API_ID = int(getenv("API_ID", "13976276"))
API_HASH = getenv("API_HASH", "7f024cbc744a2f44569c3641b5ccecb7")
BOT_TOKEN = getenv("BOT_TOKEN", "6052195748:AAFpuknQjZ9OOnqoTKoL2515BhhneWW_ZRI")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.flmdtda.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001848959319"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝄟⃝🥀⃟🇹‌𝐎𝐗𝐈𝐂⍣⃝🇲‌𝐔𝐒𝐈𝐂⃝💘")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6020570673").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "d0fea027-5831-437c-9bcd-dfbc9f373fe7")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ICC-TG-BOT/DEVIL-ICC-MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "bikash")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TOXIC_UPDATES_OFFICIAL")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/indian_chatting_club_offical")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", True)
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bc6d9e1b0269481ab87e83a8a42f5322")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "bb132b5578944891aa02826e02435576")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAFWa6YI-kbj9NJtyelg_1RVgpRkDTJeTqkQuQ-abcODRPUhjjvAo4mYtIhOCkKjS4T0jLRrCyQ_icH5bZtjfJhk216R9kLnYDwbsr5Zb8GtAU8wPCIhaQOYmzzgN7LIzE8lBUTNNcuQg7mk98VThELH7dSNbogjN4boAP7Ojs83GzTy_sVCb6rn2bCEsGEkggpKC_Qu6jTeqdgZ0dK8jbZCbRWPUcoisT-X2iMuxwHaRq_521TcWcrme2O5x-LHzgMmkiBu61jPB-P_PnbjU3Htn5jUX3ved3TxEZUJtMBILW1XdJiHKAnATokJs4fvA-D83luJEhjYgClMGr1uae2AAAAAUgLerAA")
STRING2 = getenv("STRING_SESSION2", "BQAFWa6YI-kbj9NJtyelg_1RVgpRkDTJeTqkQuQ-abcODRPUhjjvAo4mYtIhOCkKjS4T0jLRrCyQ_icH5bZtjfJhk216R9kLnYDwbsr5Zb8GtAU8wPCIhaQOYmzzgN7LIzE8lBUTNNcuQg7mk98VThELH7dSNbogjN4boAP7Ojs83GzTy_sVCb6rn2bCEsGEkggpKC_Qu6jTeqdgZ0dK8jbZCbRWPUcoisT-X2iMuxwHaRq_521TcWcrme2O5x-LHzgMmkiBu61jPB-P_PnbjU3Htn5jUX3ved3TxEZUJtMBILW1XdJiHKAnATokJs4fvA-D83luJEhjYgClMGr1uae2AAAAAUgLerAA")
STRING3 = getenv("STRING_SESSION3", "BQAFWa6YI-kbj9NJtyelg_1RVgpRkDTJeTqkQuQ-abcODRPUhjjvAo4mYtIhOCkKjS4T0jLRrCyQ_icH5bZtjfJhk216R9kLnYDwbsr5Zb8GtAU8wPCIhaQOYmzzgN7LIzE8lBUTNNcuQg7mk98VThELH7dSNbogjN4boAP7Ojs83GzTy_sVCb6rn2bCEsGEkggpKC_Qu6jTeqdgZ0dK8jbZCbRWPUcoisT-X2iMuxwHaRq_521TcWcrme2O5x-LHzgMmkiBu61jPB-P_PnbjU3Htn5jUX3ved3TxEZUJtMBILW1XdJiHKAnATokJs4fvA-D83luJEhjYgClMGr1uae2AAAAAUgLerAA")
STRING4 = getenv("STRING_SESSION4", "BQAFWa6YI-kbj9NJtyelg_1RVgpRkDTJeTqkQuQ-abcODRPUhjjvAo4mYtIhOCkKjS4T0jLRrCyQ_icH5bZtjfJhk216R9kLnYDwbsr5Zb8GtAU8wPCIhaQOYmzzgN7LIzE8lBUTNNcuQg7mk98VThELH7dSNbogjN4boAP7Ojs83GzTy_sVCb6rn2bCEsGEkggpKC_Qu6jTeqdgZ0dK8jbZCbRWPUcoisT-X2iMuxwHaRq_521TcWcrme2O5x-LHzgMmkiBu61jPB-P_PnbjU3Htn5jUX3ved3TxEZUJtMBILW1XdJiHKAnATokJs4fvA-D83luJEhjYgClMGr1uae2AAAAAUgLerAA")
STRING5 = getenv("STRING_SESSION5", "BQAFWa6YI-kbj9NJtyelg_1RVgpRkDTJeTqkQuQ-abcODRPUhjjvAo4mYtIhOCkKjS4T0jLRrCyQ_icH5bZtjfJhk216R9kLnYDwbsr5Zb8GtAU8wPCIhaQOYmzzgN7LIzE8lBUTNNcuQg7mk98VThELH7dSNbogjN4boAP7Ojs83GzTy_sVCb6rn2bCEsGEkggpKC_Qu6jTeqdgZ0dK8jbZCbRWPUcoisT-X2iMuxwHaRq_521TcWcrme2O5x-LHzgMmkiBu61jPB-P_PnbjU3Htn5jUX3ved3TxEZUJtMBILW1XdJiHKAnATokJs4fvA-D83luJEhjYgClMGr1uae2AAAAAUgLerAA")

############################
COMMAND_PREFIXES.append('')
OWNER_ID.append(1439222689)
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg")

PLAYLIST_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
GLOBAL_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"

if START_IMG_URL:
    if START_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg"
