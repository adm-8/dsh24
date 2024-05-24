from config.pgdb import PG_DB_URI
from telegram import Update
from telegram.ext import ContextTypes
import psycopg
import json

from config.logs import logger_file_path
from utils.logs import get_logger
logger = get_logger(file_path=logger_file_path)


def execute_sql(sql: str, data):
    logger.info("Executing SQL:", sql)
    logger.info("data = ", data)
    with psycopg.connect(PG_DB_URI) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql, data)
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error(e)


def log_message(update: Update, context: ContextTypes):
    # Преобразуем объект
    update_obj = json.dumps(update.to_dict())

    # Поулчаем айдишники
    user_id = update.message.from_user.id
    msg_id = update.update_id

    execute_sql("INSERT INTO app.messages (id, user_id, body) VALUES(%s, %s, %s)", (msg_id, user_id, update_obj))
