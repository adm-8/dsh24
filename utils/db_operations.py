from config.pgdb import PG_DB_URI
from telegram import Update
from telegram.ext import ContextTypes


def log_message(update: Update, context: ContextTypes):
    print(PG_DB_URI)
    print(update)
    print(context)
