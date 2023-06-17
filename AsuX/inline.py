from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch

from lokesh_dausa.config import GROUP_SUPPORT as dausa_123


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


def audio_markup(user_id):
    buttons = [
        [
            InlineKeyboardButton(text="• ᴍᴇɴᴜ", callback_data=f"cbmenu | {user_id}"),
            InlineKeyboardButton(text="• ɪɴʟɪɴᴇ", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="• ᴜᴩᴅᴀᴛᴇs", url=f"https://t.me/{dausa_123}"),
            InlineKeyboardButton(text="• ᴄʟᴏsᴇ", callback_data=f"cls"),
        ],
    ]
    return buttons


def stream_markup(user_id, dlurl):
    buttons = [
        [
            InlineKeyboardButton(text="II", callback_data=f"cbpause | {user_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"cbresume | {user_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"cbskip | {user_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"cbstop | {user_id}"),
        ],
        [
            InlineKeyboardButton(text="• ᴍᴇɴᴜ •", switch_inline_query_current_chat=""),
            InlineKeyboardButton(text="• ʏᴏᴜᴛᴜʙᴇ •", url=f"{dlurl}"),
        ],
        [
            InlineKeyboardButton(text="ᴜᴩᴅᴀᴛᴇs", url=f"https://t.me/{dausa_123}"),
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data=f"cls"),
        ],
    ]
    return buttons


def menu_markup(user_id):
    buttons = [
        [
            InlineKeyboardButton(text="II", callback_data=f"cbpause | {user_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"cbresume | {user_id}"),
        ],
        [
            InlineKeyboardButton(text="‣‣I", callback_data=f"cbskip | {user_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"cbstop | {user_id}"),
        ],
        [
            InlineKeyboardButton(text="🔇", callback_data=f"cbmute | {user_id}"),
            InlineKeyboardButton(text="🏡", url=f"https://t.me/{dausa_123}"),
            InlineKeyboardButton(text="🔊", callback_data=f"cbunmute | {user_id}"),
        ],
    ]
    return buttons


def song_download_markup(videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="⬇️ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}",
            ),
            InlineKeyboardButton(
                text="⬇️ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(text="• ᴜᴩᴅᴀᴛᴇs", url=f"https://t.me/{dausa_123}"),
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ",
                callback_data="cbhome",
            ),
        ],
    ]
    return buttons


close_mark = InlineKeyboardMarkup(
    [[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="cls")]]
)


back_mark = InlineKeyboardMarkup(
    [[InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data="cbmenu")]]
)
