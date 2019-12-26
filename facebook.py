from dotenv import load_dotenv
import os
import requests
import argparse

load_dotenv()
facebook_token = os.getenv('FACEBOOK_TOKEN')

def post_facebook(image_url,text):
     url = 'https://graph.facebook.com/v5.0/2512489632341360/photos'
     params = {
          'caption': text,
          'url': image_url,
          'access_token': facebook_token,
     }
     response = requests.post(url, params=params)
     response.raise_for_status()
     return response

if __name__=='__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('image_url', help='Введите ссылку на изображения')
     parser.add_argument('text', help='Введите текст к изображению')
     args = parser.parse_args()
     post_facebook(args.image_url, args.text)