from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = 18641799
    API_HASH = "2027706706fd39baf84c01ff5b95a6a6"
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = "6338530204:AAFdMwnT4xv8uAcJUlbvTw3A1BwmUyhqM80"
    OWNER_ID = 
    OWNER_USERNAME = "KoraXD"
    SUPPORT_CHAT = "YujiXSupport"
    LOGGER_ID = -1002142057592
    MONGO_URI = "mongodb+srv://Jujutsu:Jujutsu@jujutsu.gk8fhv9.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME = "Yuki"
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
