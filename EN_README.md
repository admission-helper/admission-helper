# admission-helper

VK bot for assistance in enrolling in P.G. Demidov University

## Install

- Windows:  
```console
$ pip install -r requirements.txt  
```
- Linux/Mac:  
```console
$ pip3 install -r requirements.txt  
```
## Using

- VK-bot:  
   * create file ___admission-helper/config.py___
   * get token vk.com/dev/access_token
   * paste into token var

```python
token = 'API_KEY'  
```

- Without VK:  
_chat_bot/main.py_

```python
start(response, model)
```