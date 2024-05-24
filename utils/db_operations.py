from config.pgdb import PG_DB_URI
from telegram import Update
from telegram.ext import ContextTypes
import psycopg
import json

# TODO: Добавить логирование через Logger


def execute_sql(sql: str):
    with psycopg.connect(PG_DB_URI) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql)
                conn.commit()
            except Exception as e:
                conn.rollback()


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
