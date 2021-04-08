import aiohttp
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from bot.config import settings
from bot.schema import Update, MessageReply
from bot.util import debug

load_dotenv()

app = FastAPI()


@app.get("/settings/")
async def handle_settings():
    debug(settings)
    return settings


@app.post("/webhook/")
async def tg_webhook(update: Update):
    try:
        reply = MessageReply(
            chat_id=update.message.chat.id,
            text=update.message.text.capitalize(),
        )
        async with aiohttp.ClientSession() as sesss:
            url = f"https://api.telegram.org/bot{settings.bot_token}/sendMessage"
            async with  sesss.post(url, json=reply.dict()) as resp:
                payload = await resp.json()
                debug(resp, payload)
    finally:
        return {"ok": True}
