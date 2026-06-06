import os
import configparser
from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

load_dotenv()
# var_name = os.getenv("var_name")
URL_UJIN = os.getenv("url_ujin")
APP_URL = os.getenv("app_url")

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_FILE = BASE_DIR / "config.ini"

config = configparser.ConfigParser()

if CONFIG_FILE.exists():
    config.read(CONFIG_FILE, encoding="utf-8")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    config.get("database", "url", fallback="sqlite:///./db.sqlite3")
)

