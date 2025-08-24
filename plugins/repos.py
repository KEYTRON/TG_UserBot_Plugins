# Coded by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo


import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/fb4807a43ec085f0996c3.jpg"
pm_caption = "`Repositories of` **@YourUsername**\n"
pm_caption += "**GitHub:** `https://github.com/YourUsername`\n\n"
pm_caption += "**Project1:** `https://github.com/YourUsername/Project1`\n"
pm_caption += "**Project2:** `https://github.com/YourUsername/Project2`\n"
pm_caption += "**Project3:** `https://github.com/YourUsername/Project3`\n"
pm_caption += "**Project4:** `https://github.com/YourUsername/Project4`\n"
pm_caption += "**Project5:** `https://github.com/YourUsername/Project5`\n"
pm_caption += "**Project6:** `https://github.com/YourUsername/Project6`\n"
pm_caption += "**Project7:** `https://github.com/YourUsername/Project7`\n"
pm_caption += "**Project8:** `https://github.com/YourUsername/Project8`\n"
pm_caption += "**Project9:** `https://github.com/YourUsername/Project9`\n"
pm_caption += "**Project10:** `https://github.com/YourUsername/Project10`\n"
pm_caption += "**Project11:** `https://github.com/YourUsername/Project11`\n"
pm_caption += "**Project12:** `https://github.com/YourUsername/Project12`\n"
pm_caption += "**Project13:** `https://github.com/YourUsername/Project13`\n"
@borg.on(admin_cmd(pattern=r"repos"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
