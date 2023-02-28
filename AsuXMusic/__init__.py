from pyrogram import Client
from AsuXMusic.config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "AsuXmusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AsuXMusic.Player"),
    )

Abishnoi = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(Abishnoi,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(Abishnoi, overload_quiet_mode=True)

with Client("AsuXMusic", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with Abishnoi as app:
    akboss = app.get_me()# ABISHNOI1M