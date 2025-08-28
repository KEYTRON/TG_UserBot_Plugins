# UserBot Configuration File
# Edit these values according to your setup

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API credentials
API_ID = os.getenv("API_ID", "your_api_id_here")
API_HASH = os.getenv("API_HASH", "your_api_hash_here")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")

# UserBot settings
ALIVE_NAME = os.getenv("ALIVE_NAME", "Your Name")
CUSTOM_PMPERMIT = os.getenv("CUSTOM_PMPERMIT", "Custom PM permit message")
PMPERMIT_PIC = os.getenv("PMPERMIT_PIC", None)

# Group settings
PRIVATE_GROUP_ID = os.getenv("PRIVATE_GROUP_ID", None)
PLUGIN_CHANNEL = os.getenv("PLUGIN_CHANNEL", None)

# Custom settings
CUSTOM_AFK = os.getenv("CUSTOM_AFK", "Custom AFK message")
CUSTOM_SLEEP = os.getenv("CUSTOM_SLEEP", "Custom sleep message")

# Replace these with your actual information
YOUR_ID = 123456789  # Your Telegram ID
YOUR_USERNAME = "YourUsername"  # Your Telegram username
YOUR_NAME = "Your Name"  # Your display name
YOUR_GROUP = "YourGroup"  # Your group username
YOUR_GITHUB = "YourUsername"  # Your GitHub username