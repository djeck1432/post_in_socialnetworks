# Publication of posts on social media 
This code will help you to simplify posting on such different social networks as ```FB``` and ```VK```, and also the messenger ```Telegram```. You would be able to post not only the text, but to add a picture to the post as well. 

# How to install
Python3 have to be already installed. Then use pip (or pip3, there is a contravention with Python2) to install dependencies: :<br>

``` git clone https://github.com/djeck1432/post_in_socialnetworks.git ```

After you downloaded the repository open a folder ```post_in_socialnetworks``` using next command: <br>

```cd post_in_socialnetworks```

Now all of the required libraries and modules have to be installed:<br>

```pip install -r requirements.txt ```<br>

Now we are ready for the script .

## Environment variables
In socail network ```Vk```:
<br>
```VK_TOKEN``` - token for ```Vk```;
<br>
```VK_PHONE```- phone number for  ```Vk```;
<br>
```VK_PASSWORD ```- password;
<br>
```VK_ALBUM_ID```- ```id``` album in your group;
<br>
```VK_OWNER_ID```- ```id``` your page;
<br>
<br>
In social network ```Fb```:
<br>
```FACEBOOK_TOKEN```-  token for ```Fb```;
<br>
```FACEBOOK_GROUP_ID```- ```id``` group for ```Fb```;
<br>
<br>
In messenger ```Telegram```:
<br>
```TELEGRAM_TOKEN```- token for ```Telegram```;
<br>
```TELEGRAM_CHAT_ID```- name of chat/chanel in ```Telegram```;
<br>

## What you need to know
Each social networks or messenger are as a self function:
<br>
```Telegram ``` - ```tg.py```;
<br>
```Facebook ``` - ```fb.py```;
<br>
```Vkontakte``` - ```vkontakte.py```;
<br>

Each of these functions takes two options:```image_path```, ```text``` :
<br> Where ```image_path``` -  is path to image, which will be download;
<br>
```text``` - text publish;<br>
<br>

# How to make a post
Do in the terminal next command:
<br>

```python3 fb.py image_path text``` 
<br>

Where ```image_path```- is path to image,
<br>
 ```text``` - text.


Done, you posted the first post in ```FB```.
<br>
If you want to post to another social network, replace ```fb.py``` to ```tg.py``` or to ```vkontakte.py```.
