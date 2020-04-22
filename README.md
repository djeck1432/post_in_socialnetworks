# Publication of posts on social media 
This code will help you to simplify posting on such different social networks as `FB` and `VK`, and also the messenger `Telegram`. You would be able to post not only the text, but to add a picture to the post as well. 

# How to install
Python3 have to be already installed. Then use pip (or pip3, there is a contravention with Python2) to install dependencies: :
```
git clone https://github.com/djeck1432/post_in_socialnetworks.git
```
After you downloaded the repository open a folder `post_in_socialnetworks` using next command:
```
cd post_in_socialnetworks
```
Now all of the required libraries and modules have to be installed:
```
pip install -r requirements.txt
```
Now we are ready for the script .

## Environment variables
In socail network `Vk`:
`VK_TOKEN` - token for `Vk`;
`VK_PHONE`- phone number for  `Vk`;
`VK_PASSWORD`- password;
`VK_ALBUM_ID`- `id` album in your group;
`VK_OWNER_ID`- `id` your page;
In social network `Fb`:
`FACEBOOK_TOKEN`-  token for `FB`;

`FACEBOOK_GROUP_ID`- `id` group for `FB`;


In messenger `Telegram`:
`TELEGRAM_TOKEN`- token for `Telegram`;
`TELEGRAM_CHAT_ID`- name of chat/chanel in `Telegram`;

## What you need to know
Each social networks or messenger are as a self function:
`Telegram` - `tg.py`;
`Facebook` - `fb.py`;
`Vkontakte` - `vkontakte.py`;

Each of these functions takes two options:`image_path`, `text`:
Where `image_path` -  is path to image, which will be download;
`text` - text publish;

# How to make a post
Do in the terminal next command:
```
python3 fb.py image_path text
``` 

Where `image_path`- is path to image,
 `text` - text.
Done, you posted the first post in `FB`.
If you want to post to another social network, replace `fb.py` to `tg.py` or to `vkontakte.py`.
