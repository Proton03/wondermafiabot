from bot import app,ADMIN,BOT_USERNAME
from pyrogram import filters, Client, idle
from pyrogram.types import ForceReply,CallbackQuery,InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant,FloodWait,PeerIdInvalid
import random
from config import ADDS,keyboard

async def acc_provide(_, m: Message, help_option: str):
    chat_id = int(help_option.split("_")[1])
    name = ADMIN
    acc= help_option.split("_")[2]
    m = await app.send_message(
                chat_id=name,
                text="Enter **Email** of acoount",reply_markup=ForceReply(selective=True))
    point = await app.listen(name, filters=None, timeout=60)
    await m.delete() 
    x = await app.send_message(
                chat_id=name,
                text="Enter **password** of account",reply_markup=ForceReply(selective=True))
    sems = await app.listen(name, filters=None, timeout=60)
    await app.send_message(
                chat_id=name,
                text="Done! payment sucsessfullβ")
    await app.send_message(
                chat_id=-1001518620432,
                text=(
                    f"β ** New Withdraw Paid**\n\n"
                    f"π **User id**: `{chat_id}`\n\n"
                    f"π° **Amount **: 5 coin\n\n"
                    f"π¦ **Account type**:{acc}\n\n"
                    f"π **Bot** : [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME}?start=1984415770)\n\n"
                    f"[βοΈ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)
    await x.delete() 
    await app.send_sticker(chat_id,"CAACAgEAAxkBAAEGVaVibOE9cIWB7CtNX4kdJnH9_M9M8wAC6wcAAuN4BAABnwXByysQy_ceBA",reply_markup=keyboard)
    await app.send_message(
                chat_id=chat_id,
                text=(
                    f"π¬ Hello sir this your {acc} Account \n\n"
                    f"π§ **Email** : `{point.text}`\n"
                    f"π **Password** :`{sems.text}`\n\n"
                    f"[βοΈ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)
    return 

async def contact_admin(_, m: Message, help_option: str):
    chat_id = int(help_option.split("_")[1])
    question = help_option.split("_")[2]
    name = ADMIN
    m = await app.send_message(
                chat_id=name,
                text="Enter message here",reply_markup=ForceReply(selective=True))
    point = await app.listen(name, filters=None, timeout=60)
    await app.send_message(
                chat_id=name,
                text="Done! Message was sent user DM.")
    await m.delete() 
    await app.send_message(
         chat_id=chat_id,
                text=(f"""
π­ <u>**Message From Admin**</u>

πΉ Question:{question}
πΉ Answer : {point.text}  """))
    return     