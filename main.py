#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import random
from student import full_info
from commands import *

#login, password='login','password'
# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()
token ='18190ed5e15e643fc50cc395008ffa023d7711e9ae395b8d33e7d54066c1317feba0ed9128140b57d7354'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

text_history = ["Вы и так в самом низу"]

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    response = response.lower()

    if response == 'старт':
        keyboard = start_button(keyboard)

    elif response == "назад":
        keyboard = keyboard_history[-1]

    elif response == "приёмная комиссия":
        text_history.append("старт")
        keyboard = sc(keyboard)

    elif response == "информация для абитуриентов":
        keyboard = sc_info(keyboard)

    elif response == "контакты приёмной комиссии":
        keyboard = sc_contacts(keyboard)

    elif response == 'узнать свой рейтинг':
        history.append('старт')

    elif response == 'адрес':
    	keyboard = back(keyboard)

    elif response == 'телефон':
        keyboard = back(keyboard)

    elif response == 'email':
        keyboard = back(keyboard)

    elif response == 'skype':
        keyboard = back(keyboard)

    elif response == 'телефон (для иностранных граждан)':
        keyboard = back(keyboard)

    elif response == 'адрес (для иностранных граждан)':
        keyboard = back(keyboard)

    elif response == 'Контакты приёмной комиссии':
    	keyboard = sc_contacts(keyboard)

    elif response == 'информация по факультетам':
        keyboard = info_button(keyboard)

    elif response == 'математический':
        keyboard.add_button('Специальности', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Общая информация', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Преимущества', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

    elif response == 'специальности':
        keyboard.add_button('Математика и компьютерные науки', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Информационная безопасность', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Прикладная математика и информатика', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

    elif response == 'общая информация':
        keyboard.add_button('День открытых дверей', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Школьникам', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Контакты', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

    elif response == 'преимущества':
        keyboard.add_button('Кружки', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Кафедры', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Семинары', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)


    elif response == 'закрыть':
        #print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        #print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        #print('Текст сообщения: ' + str(event.text))
        #print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            # if response == "котики":
            #     attachment = get_pictures.get(vk_session, -130670107, session_api)
            #     send_message(vk_session, 'user_id', event.user_id, message='Держи котиков!', attachment=attachment, keyboard=keyboard)
            if response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)

            elif response == "старт":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды:', keyboard=keyboard)

            elif response == "назад":
                send_message(vk_session, 'user_id', event.user_id, message= text_history[-1], keyboard=keyboard)

            elif response == "вопрос":
                send_message(vk_session, 'user_id', event.user_id, message= "Зайдайте мне вопрос. Я отвечу в течение дня.", keyboard=keyboard)

            elif response == "приёмная комиссия":
                send_message(vk_session, 'user_id', event.user_id, message= 'Приёмная комиссия:', keyboard=keyboard)

            elif response == "информация для абитуриентов":
                send_message(vk_session, 'user_id', event.user_id, message= 'Информация для абитуриентов:', keyboard=keyboard)

            elif response == "контакты приёмной комиссии":
                send_message(vk_session, 'user_id', event.user_id, message= 'Контакты приёмной комиссии:', keyboard=keyboard)

            elif response == "адрес":
                send_message(vk_session, 'user_id', event.user_id, message="150000, г. Ярославль, ул.Кирова 8/10, каб. 102", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message='Как до нас добраться:', keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message=' Проезд от вокзала «Ярославль-Главный» троллейбусом №1 до остановки «пл. Волкова» или Любым видом общественного транспорта до остановки «пл. Богоявления»', keyboard=keyboard)

            elif response == "телефон":
                send_message(vk_session, 'user_id', event.user_id, message= '+7(4852)30-32-10, 78-85-33', keyboard=keyboard)

            elif response == "email":
                send_message(vk_session, 'user_id', event.user_id, message= 'priem@uniyar.ac.ru', keyboard=keyboard)

            elif response == "skype":
                send_message(vk_session, 'user_id', event.user_id, message= 'priem_YarGU', keyboard=keyboard)

            elif response == "телефон (для иностранных граждан)":
                send_message(vk_session, 'user_id', event.user_id, message= '+7(4852)79-77-45, 79-77-46', keyboard=keyboard)

            elif response == "email (для иностранных граждан)":
                send_message(vk_session, 'user_id', event.user_id, message= 'depint@uniyar.ac.ru', keyboard=keyboard)

            elif response == "информация по факультетам":
                send_message(vk_session, 'user_id', event.user_id, message= 'Факультеты:', keyboard=keyboard)

            elif response == "Узнать свой рейтинг":
                send_message(vk_session, 'user_id', event.user_id, message= full_info('Студент 1'))

            elif response == "математический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Математический:', keyboard=keyboard)

            elif response == "специальности":
                send_message(vk_session, 'user_id', event.user_id, message= 'Специальности:', keyboard=keyboard)

            elif response == "общая информация":
                send_message(vk_session, 'user_id', event.user_id, message= 'Общая информация:', keyboard=keyboard)

            elif response == "преимущества":
                send_message(vk_session, 'user_id', event.user_id, message= 'Преимущества:', keyboard=keyboard)

            elif response == 'команды':
                send_message(vk_session, 'user_id', event.user_id, message='Список команд бота: \n \n 1)Команда1 \n 2)Команда2')

            elif response == 'закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)

            elif response == "Можно ли оплачивать учёбу не по семестру, а по месячно?":
                send_message(vk_session, 'user_id', event.user_id, message= full_info('Студент 1'))



        # elif event.from_chat :
        #     if response == "котики":
        #         attachment = get_pictures.get(vk_session, -130670107, session_api)
        #         print(attachment)
        #         send_message(vk_session, 'chat_id', event.chat_id, message='Держите котиков!', attachment= attachment)
        #print('-' * 30)
