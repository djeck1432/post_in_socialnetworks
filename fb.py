from dotenv import load_dotenv
import os
import argparse
import facebook




def post_facebook(image_path, text):
    graph = facebook.GraphAPI(access_token=facebook_token, version='3.1')
    with open(image_path, 'rb') as image:
        graph.put_photo(image=image, album_path='2512489632341360' + '/photos', message=text)


if __name__ == '__main__':
    load_dotenv()
    facebook_token = os.getenv('FACEBOOK_TOKEN')

    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', help='Введите ссылку на изображения')
    parser.add_argument('text', help='Введите текст к изображению')
    args = parser.parse_args()
    post_facebook(args.image_path, args.text)
