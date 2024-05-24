from telegram import Update
from config.openai_client import client
from utils.db_operations import log_message


async def chatgpt_reply(update: Update, context):
    # логируем сообщение
    await log_message(update=update, context=context)
    # текст входящего сообщения
    text = update.message.text

    # запрос
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        max_tokens=1024,
        temperature=0.5,
    )

    # ответ
    reply = response.choices[0].message.content.strip()

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)   
    
    print("user:", text)
    print("assistant:", reply)