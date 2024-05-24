from config.pgdb import PG_DB_URI
from telegram import Update
from telegram.ext import ContextTypes
import psycopg

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
    execute_sql("select 1")
