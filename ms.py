import os
import logging
import psycopg2
import telebot
import instaloader
from TikTokApi import TikTokApi

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Задаем токен
TOKEN = '7941402803:AAF0wiMrS2LhQ9gYnz_Vh8z7N59LxYED9EM'
bot = telebot.TeleBot(TOKEN)

# Подключение к базе данных
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Отправь мне ссылку на видео из Instagram или TikTok, и я его скачаю.')

def download_instagram_video(url):
    L = instaloader.Instaloader()
    # Здесь добавьте код для загрузки видео
    return "Путь к загруженному видео"

def download_tiktok_video(url):
    api = TikTokApi.get_instance()
    # Здесь добавьте код для загрузки видео
    return "Путь к загруженному видео"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if 'instagram.com' in url:
        video_path = download_instagram_video(url)
    elif 'tiktok.com' in url:
        video_path = download_tiktok_video(url)
    else:
        bot.reply_to(message, 'Неверная ссылка! Пожалуйста, отправь ссылку на видео из Instagram или TikTok.')
        return

    with open(video_path, 'rb') as video_file:
        bot.send_video(message.chat.id, video_file)

if __name__ == '__main__':
    bot.polling()
