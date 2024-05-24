import json

from telegram import Update,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from utils.db_operations import log_message

async def start_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # логируем сообщение
    await log_message(update=update, context=context)

    # объект обновления
    #update_obj = json.dumps(update.to_dict(), indent=4)

    # ответ
    reply = "Привет! Я бот-помощник. Напиши сообщение и я спрошу у ChatGPT. Можешь даже отправить картинку с запросом.\n" + \
            "А если отправить картинку с изображением таблицы без подписи, то я верну SQL-скрипт для создания этой таблицы.\n" + \
            "А ещё я умею говорить 'Привет' по команде /hello"
    #reply = "*update object*\n\n" + "```json\n" + update_obj + "\n```"

    # перенаправление ответа в Telegram
    #await update.message.reply_text(reply, parse_mode="Markdown")
    await update.message.reply_text(reply)

    print("assistant:", reply)
    
async def hello_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # логируем сообщение
    await log_message(update=update, context=context)

    # ответ
    reply = f"Привет, {update.message.chat.first_name}!" 
    
    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)

    print("assistant:", reply)
    