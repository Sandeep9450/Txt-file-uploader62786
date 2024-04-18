import os

API_ID = API_ID = 26116403

API_HASH = os.environ.get("API_HASH", "f9572ff772e0ac828ce3fb1321f00e03")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6822992228:AAHAc61ZretVrDz4Ac6rkmNiPzE-te-tmiE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6822992228)

LOG = -1002002687613,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6822992228").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


