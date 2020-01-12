from dotenv import load_dotenv
import vk_api
import os
import argparse


def post_vkontakte(vk_token, image_path, text):
    vk_session = vk_api.VkApi(vk_phone, vk_password)
    vk = vk_session.get_api()
    vk_session.auth()
    upload = vk_api.VkUpload(vk_session)
    owner_id = '-' + vk_owner_id
    photo = upload.photo(
        image_path,
        group_id=vk_owner_id,
        album_id=vk_album_id
    )
    attachment_photo = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
    return vk.wall.post(owner_id=owner_id, message=text, attachment=attachment_photo)


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    vk_phone = os.getenv('VK_PHONE')
    vk_password = os.getenv('VK_PASSWORD')
    vk_owner_id = os.getenv('VK_OWNER_ID')
    vk_album_id = os.getenv('VK_ALBUM_ID')

    parser = argparse.ArgumentParser(description='Введите url-изображения и текст')
    parser.add_argument('image_path', help='Введите url-изображения')
    parser.add_argument('text', help='Введите текст')
    args = parser.parse_args()
    post_vkontakte(vk_token, args.image_path, args.text)
