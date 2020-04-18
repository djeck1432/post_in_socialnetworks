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

## Переменные окружения 
В социальной сети ```Vk```:
<br>
```VK_TOKEN``` - токен доступа от ```Vk```;
<br>
```VK_PHONE```- номер телефона, на который зарегестрирован  ```Vk```;
<br>
```VK_PASSWORD ```- пароль от учетной записи;
<br>
```VK_ALBUM_ID```- ```id``` альбома в вашей группе;
<br>
```VK_OWNER_ID```- ```id``` вашей страницы;
<br>
<br>
В социальной сети ```Fb```:
<br>
```FACEBOOK_TOKEN```-  токен доступа от ```Fb```;
<br>
```FACEBOOK_GROUP_ID```- ```id``` группы в ```Fb```;
<br>
<br>
В месенджере ```Telegram```:
<br>
```TELEGRAM_TOKEN```- токен доступа от ```Telegram```;
<br>
```TELEGRAM_CHAT_ID```- имя вашего чата/канала в ```Telegram```;
<br>

## Что нужно знать

Каждая социальная сеть или мессенджер выполнен как отдельная функция
<br>
```Telegram ``` - ```tg.py```;
<br>
```Facebook ``` - ```fb.py```;
<br>
```Vkontakte``` - ```vkontakte.py```;
<br>
Каждая из этих функций принимает два параметра:```image_path```, ```text``` :
<br> где ```image_path``` - это путь к изображению, которое вы хотите загрузить;
<br>
```text``` - текст публикации;<br>
<br>

# Как сделать пост 

В терминале, выполните следующую команду:
<br>

```python3 fb.py image_path text``` 
<br>

Где вместо ```image_path```- путь к изображению,
<br>
 ```text``` - текст.


Готово, вы опубликовали первый пост в ```Fb```.
<br>
Если хотите опубликовать в другую социальную сеть, замените ```fb.py``` на ```tg.py``` или на ```vkontakte.py```.
