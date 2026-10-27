
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

BOT_NAME = "Team Skyfall"
DATABASE_PATH = "database/skyfall.db"

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN is missing. Set it in your .env file."
    )
  
