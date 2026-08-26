import os

SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "tajergo_db")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MAIN_DOMAIN = os.getenv("MAIN_DOMAIN", "saas-store-products.vercel.app")
STATIC_VERSION = os.getenv("STATIC_VERSION", "20260825.1")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is required")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is required")
