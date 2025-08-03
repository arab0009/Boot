import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = '8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0'
REDIRECT_URL = 'https://boot-eg8h.onrender.com'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("✅ تأكيد تحويل الأموال للمحفظة", url=REDIRECT_URL)
    keyboard.add(btn)

    text = (
        "💸 *مرحبًا بك في بوت التحويل بالعملات الرقمية*\n"
        "🔐 لتأكيد العملية، اضغط على الزر أدناه 👇"
    )
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode='Markdown')

print("🤖 Bot is running...")
bot.infinity_polling()
