import json

from telegram import Update,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from utils.db_operations import log_message
from config.pgdb import PG_DB_URI

async def start_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # логируем сообщение
    log_message(update=update, context=context)

    # объект обновления
    update_obj = json.dumps(update.to_dict(), indent=4)

    # ответ
    reply = "*update object*\n\n" + "```json\n" + update_obj + f"\n\n\n{PG_DB_URI}```"

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply, parse_mode="Markdown")

    print("assistant:", reply)