import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

# Get the Telegram bot token and Google API key from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Google Generative AI with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Define a start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your chatbot powered by Google Generative AI. How can I assist you?")

# Define a handler for regular messages (chatbot functionality)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Generate a response using Google Generative AI
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_message)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"An error occurred while processing your message: {str(e)}"

    # Send the generated response back to the user
    await update.message.reply_text(bot_reply)

# Main function to run the bot
def main():
    # Initialize the bot application
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
