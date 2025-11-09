import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import yt_dlp

BOT_TOKEN = "8565663576:AAFnaC-qxL2WC0ELRk8wJhDS_86BJm23gwM"

def start(update, context):
    update.message.reply_text('Hello! Video link bhejen, main download kar dunga!')

def handle_video_link(update, context):
    video_url = update.message.text
    
    try:
        # Video download logic
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_file = ydl.prepare_filename(info)
        
        # Video send karein
        with open(video_file, 'rb') as video:
            context.bot.send_video(
                chat_id=update.effective_chat.id, 
                video=video,
                caption=f"Downloaded: {info.get('title', 'Video')}"
            )
    
    except Exception as e:
        update.message.reply_text(f'Error: {str(e)}')

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_video_link))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
