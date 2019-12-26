from dotenv import load_dotenv
import vk_api
import os
import argparse




def post_vkontakte(url_image, text):
    vk_session = vk_api.VkApi(vk_phone,vk_password)
    vk = vk_session.get_api()
    vk_session.auth()
    owner_id = -190053871
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
            url_image,
            group_id =190053871,
            album_id=269466802
        )
    vk_photo_url = 'https://vk.com/photo{}_{}'.format(
    photo[0]['owner_id'], photo[0]['id']
    )
    attachment_photo = 'photo{}_{}'.format(photo[0]['owner_id'],photo[0]['id'])
    print(vk.wall.post(owner_id=owner_id, message=text, attachment=attachment_photo))

if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    vk_phone = os.getenv('VK_PHONE')
    vk_password = os.getenv('VK_PASSWORD')

    parser = argparse.ArgumentParser(description='Введите url-изображения и текст')
    parser.add_argument('url_image', help='Введите url-изображения')
    parser.add_argument('text', help='Введите текст')
    args = parser.parse_args()
    post_vkontakte(args.url_image, args.text)

