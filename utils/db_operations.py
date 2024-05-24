from config.pgdb import PG_DB_URI
from telegram import Update
from telegram.ext import ContextTypes
import psycopg
import json

from config.logs import logger_file_path
from utils.logs import get_logger
logger = get_logger(file_path=logger_file_path)


async def execute_sql(sql: str, data):
    with psycopg.connect(PG_DB_URI) as conn:
        with conn.cursor() as cur:
            try:
                logger.info("Executing SQL")
                cur.execute(sql, data)

                logger.info("Commit data...")
                conn.commit()

                logger.info("SQL executed successfully!")
            except Exception as e:
                conn.rollback()
                logger.info(f"Error: {e}")


async def log_message(update: Update, context: ContextTypes):
    # Преобразуем объект
    update_obj = json.dumps(update.to_dict())

    # Поулчаем айдишники
    user_id = update.message.from_user.id
    msg_id = update.update_id

    logger.info(f"Logging user message:\nuser_id = {user_id}\n msg_id={msg_id}\nupdate_obj={update_obj}")

    await execute_sql("INSERT INTO app.messages (id, user_id, body, msg_dttm) VALUES(%s, %s, %s, now())", (msg_id, user_id, update_obj))
