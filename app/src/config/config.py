import os
import configparser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_FILE = BASE_DIR / "config.ini"

config = configparser.ConfigParser()

if CONFIG_FILE.exists():
    config.read(CONFIG_FILE, encoding="utf-8")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    config.get("database", "url", fallback="sqlite:///./db.sqlite3")
)

