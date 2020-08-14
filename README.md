# admission-helper

[English](github.com/yargtu/admission-helper/EN_README.md)  

ВК-бот для помощи при поступлении в ЯрГУ

## Установка

- Windows:  
```console
$ pip install -r requirements.txt  
```
- Linux/Mac:  
```console
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

- Без привязки к ВК  
_chat_bot/main.py_

```python
start(response, model)
```