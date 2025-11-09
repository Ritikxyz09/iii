import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import yt_dlp

# Bot token yahan dalen
BOT_TOKEN = "8565663576:AAFnaC-qxL2WC0ELRk8wJhDS_86BJm23gwM"

def start(update, context):
    update.message.reply_text('Hello! Video link bhejen, main download kar dunga!')

def handle_video_link(update, context):
    video_url = update.message.text
    
    try:
        # Video download logic
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_file = ydl.prepare_filename(info)
        
        # Video send karein
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(video_file, 'rb'))
    
    except Exception as e:
        update.message.reply_text(f'Error: {str(e)}')

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_video_link))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
