import json
import os

import vk_api
import random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# from student import full_info
# from memo import *
# from commands import *
from config import token
from chat_bot.main import get_model, start