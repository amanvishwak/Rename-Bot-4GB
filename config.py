import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "22182189"))
API_HASH = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8182224498:AAG4leCVgBgVEYUmyBzS_N5cK_1OSeRD0mg")
ADMIN = int(os.environ.get("ADMIN", "5977931010"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "AV_BOTz_UPDATE")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002110971750"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aman991932:aman@cluster0.18hv15a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "cluster0")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ad48ac09b1e6f30d2dae4.jpg")

