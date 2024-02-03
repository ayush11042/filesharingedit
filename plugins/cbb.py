#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴄʀᴇᴀᴛᴏʀ : <a href='https://telegram.me/GOTFLiXownerbot'>ᴀʏᴜꜱʜ</a>\n○ ʟᴀɴɢᴜᴀɢᴇ : <code>ᴘʏᴛʜᴏɴ3</code>\n○ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ ᴀꜱʏɴᴄɪᴏ {__version__}</a>\n○ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://telegram.me/GOTFLiXownerbot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n○ ᴄʜᴀɴɴᴇʟ : <a href='https://telegram.me/GOTFLiX'>ɢᴏᴛꜰʟɪx</a>\n○ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href='https://telegram.me/GOTFLiXGROUP'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
