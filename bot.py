import os
import django
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_game.settings')
django.setup()

def start_game(update, context):
    user = update.message.from_user
    web_app_url = f"https://yourdomain.com/?user_id={user.id}"
    
    keyboard = [
        [InlineKeyboardButton("Play the Game 🎮", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Click the button below to start playing!", reply_markup=reply_markup)

def main():
    updater = Updater("YOUR_BOT_TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_game))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
