# admission-helper

ВК-бот для помощи при поступлении в ЯрГУ

Синхронная версия на vk_api в chat_bot

Начата работа над асинхронной версией в папке new_bot

## Установка

- Windows:  
```console
$ pip install virtualenv
$ venv env
$ env/scripts/activate.ps1
$ pip install -r requirements.txt  
```
- Linux/Mac:  
```console
$ pip3 install virtualenv
$ venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt  
```

***
## Использование

- ВК-бот:  
   * создайте файл ___admission-helper/config.py___
   * получите токен vk.com/dev/access_token
   * вставьте его

```python
token = 'API_KEY'  
```