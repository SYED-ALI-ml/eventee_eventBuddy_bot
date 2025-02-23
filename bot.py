import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

access_token = os.getenv('BOT_ACCESS_TOKEN')
bot_username = os.getenv('BOT_USERNAME')

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = "Hello 👋 I am Eventee bot.\nI shall update you about the events.\n\nAdd me to your groups and use /link command to get event updates in that group."
    await update.message.reply_text(response)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = "I will give you regular updates about the events.\n\nYou can control me by sending these commands:\n\n/start - Start bot\n/help - Get command list\n/link - Link group to EventBuddy"
    await update.message.reply_text(response)

async def link_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        unique_code = context.args[0]
        chat_id = update.message.chat.id
        print(f'unique_code: {unique_code}, chat_id: {chat_id}')
    else:
        response = "You need to provide the unique code.\nExample: /link unique_code"
        await update.message.reply_text(response)

def main():
    # Build bot
    print('Starting bot... ')
    app = Application.builder().token(access_token).build()

    # Handle commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('link', link_command))

    print('Polling... ')
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()
