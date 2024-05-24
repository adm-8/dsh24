import re

from telegram import Update
from config.openai_client import client
from utils.helpers import image_to_base64
from utils.db_operations import log_message

async def image_file_reply(update, context):
    # логируем сообщение
    log_message(update=update, context=context)

    # Получение объекта File
    image_file = await context.bot.get_file(update.message.photo[-1].file_id)
    print("image_file -> ", image_file)

    # Получение подписи к изображению
    caption = update.message.caption
    print("caption -> ", caption)
    if caption is not None:
        query = caption
    else:
        query = "Create DDL SQL-query for PostgreSQL for a table on the screen"

    # обработка изображения
    description = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query,
                    },
                    {
                        "type": "image_url",
                        "image_url":{
                            "url": image_file.file_path,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    if caption is not None:
        # ответ
        reply = description.choices[0].message.content.strip()
        print("assistant:", reply)

        # перенаправление ответа в Telegram
        await update.message.reply_text(reply)
    
    else:
        # ответ
        reply = description.choices[0].message.content.strip()
        reply_match = re.search("CREATE[\w*\W*]*;", reply)
        try:
            reply_ddl = reply_match.group()
            print("assistant:", reply_ddl)
            with open('ddl.sql', 'w') as f:
                f.write(reply_ddl)

            # перенаправление ответа в Telegram
            chat_id = update.message.chat_id
            await context.bot.send_document(chat_id, 'ddl.sql') 
            await update.message.reply_text(reply_ddl)
        except:
            await update.message.reply_text("Не удалось распознать таблицу")