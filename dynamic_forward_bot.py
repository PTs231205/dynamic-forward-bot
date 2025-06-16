from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

API_TOKEN = "7671786592:AAHhVKBGobpn2gwUFIOoafY1st7kj080huo"

async def show_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if chat:
        chat_id = chat.id
        try:
            await context.bot.send_message(chat_id=chat_id, text=f"✅ This chat ID is: `{chat_id}`", parse_mode="Markdown")
        except Exception as e:
            print(f"❌ Error sending message: {e}")
    else:
        print("❌ No chat info found in update.")

def main():
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, show_chat_id))
    print("🔄 Bot is running... send message or forward from channel.")
    app.run_polling()

if __name__ == "__main__":
    main()