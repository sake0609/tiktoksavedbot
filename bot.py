import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import instaloader
from TikTokApi import TikTokApi

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Задаем токен
TOKEN = '7941402803:AAF0wiMrS2LhQ9gYnz_Vh8z7N59LxYED9EM'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне ссылку на видео из Instagram или TikTok, и я его скачаю.')

def download_instagram_video(url):
    L = instaloader.Instaloader()
    # Здесь добавь код для загрузки видео
    return "Путь к загруженному видео"

def download_tiktok_video(url):
    api = TikTokApi.get_instance()
    # Здесь добавь код для загрузки видео
    return "Путь к загруженному видео"

def handle_message(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    if 'instagram.com' in url:
        video_path = download_instagram_video(url)
    elif 'tiktok.com' in url:
        video_path = download_tiktok_video(url)
    else:
        update.message.reply_text('Неверная ссылка! Пожалуйста, отправь ссылку на видео из Instagram или TikTok.')
        return

    with open(video_path, 'rb') as video_file:
        update.message.reply_video(video_file)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
