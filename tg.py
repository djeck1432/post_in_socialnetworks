from dotenv import load_dotenv
import os
import telegram
import argparse

load_dotenv()
telegram_token = os.getenv('TELEGRAM_TOKEN')
bot = telegram.Bot(token=telegram_token)

def post_telegram(image_url,text):
    bot.send_message(chat_id='@test_djeck1432',text=text)
    bot.send_photo(chat_id='@test_djeck1432',photo=open(image_url, 'rb'))

if __name__=='__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=telegram_token)

    parser = argparse.ArgumentParser()
    parser.add_argument('image_url', help='Введите ссылку на изображения')
    parser.add_argument('text', help='Введите текст к изображению')
    args = parser.parse_args()
    post_telegram(args.image_url, args.text)
