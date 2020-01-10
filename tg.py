from dotenv import load_dotenv
import os
import telegram
import argparse


def post_telegram(image_url, text):
    bot.send_message(chat_id=telegram_chat_id, text=text)
    with open(image_url, 'rb') as photo:
        bot.send_photo(chat_id=telegram_chat_id, photo=photo)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=telegram_token)

    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', help='Введите ссылку на изображения')
    parser.add_argument('text', help='Введите текст к изображению')
    args = parser.parse_args()
    post_telegram(args.image_path, args.text)

