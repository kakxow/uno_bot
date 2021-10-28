import os
import logging
import signal

from telegram.ext import CommandHandler, Updater, InlineQueryHandler
from telegram import InlineQueryResultPhoto, InputTextMessageContent
from dotenv import load_dotenv

from game import Uno

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

games: dict[str, Uno] = {}


def existing_game_only(f):
    def wrapper(update, context):
        if update.effective_chat.id not in games:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Game session is not created yet, use /new to create it!",
            )
        else:
            f(update, context)
    return wrapper


def group_chat_only(f):
    def wrapper(update, context):
        if update.effective_chat.type not in ("group", "supergroup"):
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Add a bot to a group and try again!",
            )
        else:
            f(update, context)
    return wrapper


@group_chat_only
@existing_game_only
def start(update, context):
    game = games[update.effective_chat.id]
    try:
        game.start_game()
    except RuntimeError:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Not enough players! Need at least 2 players to start!",
        )


@group_chat_only
def new(update, context):
    games[update.effective_chat.id] = Uno()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Game session created, anyone can /join and /start now!",
    )


@group_chat_only
@existing_game_only
def join(update, context):
    game = games[update.effective_chat.id]
    user = update.effective_user
    try:
        game.join_session(user.first_name, user.id)
    except KeyError:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You've already joined :)",
            reply_to_message_id=update.effective_message.message_id
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You successfully joined!",
            reply_to_message_id=update.effective_message.message_id
        )


def shutdown(update, context):
    os.kill(os.getpid(), signal.SIGINT)


def inline_cards(update, context):
    # query = update.inline_query.query
    # if not query:
    #     return
    img_url = "https://raw.githubusercontent.com/jh0ker/mau_mau_bot/master/images/jpg/b_0.jpg"
    thumb_url = "https://raw.githubusercontent.com/jh0ker/mau_mau_bot/master/images/thumb/b_0.jpg"
    results = list()
    results.append(
        InlineQueryResultPhoto(
            1,
            img_url,
            thumb_url,
            title="blue 0",)
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_cards)
dispatcher.add_handler(inline_caps_handler)

join_handler = CommandHandler("join", join)
new_handler = CommandHandler("new", new)
shutdown_handler = CommandHandler("shutdown", shutdown)
start_handler = CommandHandler("start", start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(join_handler)
dispatcher.add_handler(new_handler)
dispatcher.add_handler(shutdown_handler)

updater.start_polling()
