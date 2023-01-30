import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins




logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
vzq = TelegramClient('kolge', api_id, api_hash).start(bot_token=bot_token)



@vzq.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply("Aramıza Xoş gəldin 😍")

@vzq.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Səni tanimaq gözəl idi 🙃")

print("<<bot isleyir qiril>>")
vzq.run_until_disconnected()
