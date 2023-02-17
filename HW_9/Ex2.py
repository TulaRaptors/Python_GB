from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("6059575868:AAENVDYMAIVgQ64Ers8HPSDQaaLqP5eJNmc").build()


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')


app.add_handler(CommandHandler("hi", hi))
print('Server START')
app.run_polling()
