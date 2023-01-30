from telethon import TelegramClient
from telethon import events



API_ID = "12210813"
API_HASH = "e42eeae11a2f96bcfc5ec3b46a30adad"
bot_token = "5631477617:AAFrf8wg07Anl5MpmZj3LMPCEZkJw966hCM"

ged = "reddol"
app = TelegramClient('app', API_ID, API_HASH).start(bot_token=bot_token)

@app.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply("Aramıza Xoş gəldin 😍")

@app.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Səni tanimaq gözəl idi 🙃")

print("<<bot isleyir qiril>>")
app.run_until_disconnected()
