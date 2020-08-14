from main_lib import *

def json_commands():
    with open("data/structure.json", "r", encoding="utf-8") as data_file:
        commands = json.load(data_file)

    path = 'data/faculties'
    faculties = os.listdir(path)

    for faculty in faculties:
        with open(path + '/' + faculty, "r", encoding="utf-8") as data_file:
            part = json.load(data_file)
        commands['children'][1]['children'].append(part)
    
    return commands

def response_search(json, response):
    ans = [] # найденные значения

    def extract(json, ans, response):
        """Рекурсивный поиск значений в JSON"""
        if isinstance(json, dict):
            for k, v in json.items():
                if isinstance(v, (dict, list)):
                    extract(v, ans, response)
                elif k == 'text' and v.lower() == response:
                    ans.extend(json['children'])
        elif isinstance(json, list):
            for item in json:
                extract(item, ans, response)
        return ans

    results = extract(json, ans, response)
    return results

def create_keyboard(keyboard, response):
    commands = json_commands()
    messages = response_search(commands, response)
    intents = []

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

def chat_start():
    vk_session = vk_api.VkApi(token=token)
    session_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()

            keyboard = VkKeyboard()
            keyboard = create_keyboard(keyboard, response)

            commands = json_commands()
            messages = response_search(commands, response)

            if event.from_user and not event.from_me:
                if messages:
                    response = response.capitalize()
                    send_message(vk_session, 'user_id', event.user_id, message=response, keyboard=keyboard.get_keyboard())
                else:
                    model = get_model()
                    send_message(vk_session, 'user_id', event.user_id, message=chatbot_response(response, model))

chat_start()