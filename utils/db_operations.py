from config.pgdb import PG_DB_URI
from telegram import Update
from telegram.ext import ContextTypes
from utils.logs import get_logger
import psycopg
import json
from dotenv import load_dotenv
import os


load_dotenv()
logger = get_logger(file_path=os.getenv("LOGGER_FILE_PATH"))


def execute_sql(sql: str):
    logger.info("Executing SQL:", sql)
    with psycopg.connect(PG_DB_URI) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql)
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error(e)


def log_message(update: Update, context: ContextTypes):
    # Преобразуем объект
    update_obj = json.dumps(update.to_dict(), indent=4)

    # Поулчаем айдишники
    user_id = update.message.from_user.id
    msg_id = update.update_id

    execute_sql(f"""
        INSERT INTO app.messages (id, user_id, body) 
        VALUES({msg_id}, {user_id}, '{update_obj}'::json)
    """)
