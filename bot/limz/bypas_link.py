# Poweered by RKMBot and Rozakul Halim
# https://t.me/MRojeck_Lim

from asyncio import sleep
from datetime import datetime

from time import time

from pyrogram.handlers import MessageHandler
from pyrogram.filters import command
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.parse import urlparse

from bot import bot, config_dict
from bot.helper.ext_utils.bot_utils import is_url
from bot.helper.mirror_utils.download_utils.direct_link_generator import direct_link_generator
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import anno_checker, sendMessage, editMessage
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.button_build import ButtonMaker

async def direct(client, message):
    args = message.text.split()
    link = ''
    if not message.from_user:
        message.from_user = await anno_checker(message)
    if not message.from_user:
        return
    if len(args) > 1:
        link = args[1]
    elif reply_to := message.reply_to_message:
        link = reply_to.text
    else:
        link = ''
        
    if is_url(link):
        s = datetime.now()
        mess = f"<b><i>⏳  Generating direct link from</i></b> <code>{link}</code>.."
        ray = await sendMessage(message, mess1)
        try:
            res = direct_link_generator(link)
            await sleep(2)
            e = datetime.now()
            ms = (e - s).seconds
            host = urlparse(link).netloc
            if message.from_user.username:
                uname = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
            else:
                uname = f'@{message.from_user.username}'
            if uname is not None:
                cc = f'\n<b>🙎🏻‍♂️ :</b> {uname} 🆔 : <code>({message.from_user.id})</code>✨\n\n#⃣#bypass #direct #id{message.from_user.id}\n🅿️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @𝑨𝒃𝒐𝒖𝒕𝑹𝒆𝒚𝒔𝒉𝒂𝑵𝒊𝒎'
            mess3 = f"<b>🆓 <u>Original Links</u>: </b>\n<code>{link}</code>\n\n<b>💮 <u>Bypass Link</u> <code>{host}</code>: </b>\n{res}\n\n<b>⌚ Excute Finish On: </b> <code>{ms} seconds</code>" 
            await editMessage(ray, mess3 + cc)
        except Exception:
            url = "https://telegra.ph/RH-MirrorBot-05-28"
            tombol1 = [[
                    InlineKeyboardButton('💠 Supported Links', url=url),                
                ]]
            limz = InlineKeyboardMarkup(tombol1)
            await editMessage(ray, f"<b>⚠️ Sorry Your Link Currently <i>Not Supported or Not Valid</i></b>\n\n<b>🆑 Curently Supported SITES :</b> Uptobox - bayfiles - Ouo - Fembed - Streamtape - Yandisk - LinkVertise - GpLinks - AndroidDatahost - AndroidFilehost", limz)

    else:
         url = "https://telegra.ph/RH-MirrorBot-05-28"
         tombol1 = [[
                InlineKeyboardButton('💠 Supported Links', url=url),                
            ]]
         limz = InlineKeyboardMarkup(tombol1)
         await editMessage(message, f"<b>⚠️ Please Use :</b> <code>/{BotCommands.DirectCommand}</code> [Url Supported bypas link]\n\n<b>🆑 Curently Supported SITES :</b> Uptobox - bayfiles - Ouo - Fembed - Streamtape - Yandisk - LinkVertise - GpLinks - AndroidDatahost - AndroidFilehost", limz)


bot.add_handler(MessageHandler(direct, filters=command(BotCommands.DirectCommand) & CustomFilters.authorized))
