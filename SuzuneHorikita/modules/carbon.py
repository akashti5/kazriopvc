from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from SuzuneHorikita import pbot
from SuzuneHorikita.utils.errors import capture_err
from SuzuneHorikita.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/188e0de81aaec613bad4f.jpg"

@pbot.on_message(filters.command("alive"))
async def alive(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""✨ **Hᴇʏ I Am Suzune Rᴏʙᴏᴛ** 

**🧑‍💻 Powered By : [SuzuneHorikita](https://t.me/Suzune_Superbot)**
**🐍 Python Version :** `{y()}`
**📃 Library Version :** `{o}`
**♻️ Telethon Version :** `{s}`
**💥 Pyrogram Version :** `{z}`

**Create your own with click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/TheVenomXD"), 
                    InlineKeyboardButton(
                        "Support", url="https://t.me/Suzune_Support")
                ]
            ]
        )
    )
