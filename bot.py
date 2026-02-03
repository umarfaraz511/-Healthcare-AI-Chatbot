from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from telegram.request import HTTPXRequest
from src.ai_handler import AIHandler
from src.language_handler import get_text, detect_language, SUPPORTED_LANGUAGES
from config.settings import TELEGRAM_TOKEN
import asyncio

ai_handler = AIHandler()
user_languages = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_languages[user_id] = 'en'
    await update.message.reply_text(get_text('welcome', 'en'))

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton('🇬🇧 English', callback_data='lang_en')],
        [InlineKeyboardButton('🇵🇰 اردو', callback_data='lang_ur')],
        [InlineKeyboardButton('🇸🇦 العربية', callback_data='lang_ar')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('🌍 Select Language / زبان منتخب کریں / اختر اللغة:', reply_markup=reply_markup)

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    lang_code = query.data.split('_')[1]
    user_languages[user_id] = lang_code
    
    await query.edit_message_text(get_text('lang_selected', lang_code))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text
    language = user_languages.get(user_id, 'en')
    
    await update.message.reply_text('🔄 Processing...')
    
    response = await ai_handler.get_response(user_message, language)
    await update.message.reply_text(response)

def run_bot():
    # Configure request with longer timeout
    request = HTTPXRequest(
        connection_pool_size=8,
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
        pool_timeout=30.0
    )
    
    app = Application.builder().token(TELEGRAM_TOKEN).request(request).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('language', language_command))
    app.add_handler(CallbackQueryHandler(language_callback, pattern='^lang_'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print('✅ Bot configured successfully!')
    print('🔄 Connecting to Telegram...')
    
    try:
        app.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        print(f'❌ Connection error: {e}')
        print('💡 Try: 1) Check internet 2) Disable firewall 3) Use VPN')
