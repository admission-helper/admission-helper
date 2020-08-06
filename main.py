from main_lib import *

with open("json/structure.json", "r", encoding="utf-8") as data_file:
    commands = json.load(data_file)

path = 'json/faculties'
faculties = os.listdir(path)

for faculty in faculties:
    with open(path + '/' + faculty, "r", encoding="utf-8") as data_file:
        part = json.load(data_file)
    commands['children'][1]['children'].append(part)

def extract_values(obj, value):
    """Pull all values of specified value from nested JSON."""
    arr = []

    def extract(obj, arr, value):
        """Recursively search for values of value in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, value)
                elif k == 'text' and v.lower() == value:
                    arr.extend(obj['children'])
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, value)
        return arr

    results = extract(obj, arr, value)
    return results


vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def create_keyboard(keyboard, response):
    messages = extract_values(commands, response)
    intents = []
    vk_colors = {
        'POSITIVE': VkKeyboardColor.POSITIVE,
        'NEGATIVE': VkKeyboardColor.NEGATIVE,
        'PRIMARY': VkKeyboardColor.PRIMARY,
        'DEFAULT': VkKeyboardColor.DEFAULT
        }
    for message in messages:
        intents.append(message['text'])
        cur_color = message['keyboard_color']

        keyboard.add_button(message['text'], color=vk_colors[cur_color])
        keyboard.add_line()

    
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send', 
    {
        id_type: id, 'message': message, 
        'random_id': random.randint(-2147483648, +2147483648), 
        "attachment": attachment, 'keyboard': keyboard
        })

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text.lower()
        
        keyboard = VkKeyboard(one_time=False)
        keyboard = create_keyboard(keyboard, response)

        messages = extract_values(commands, response)

        if event.from_user and not event.from_me:
            if messages:
                response = response.capitalize()
                send_message(vk_session, 'user_id', event.user_id, message=response, keyboard=keyboard.get_keyboard())
                print(messages)
            else:
                model = get_model()
                send_message(vk_session, 'user_id', event.user_id, message=start(response, model))
            
        