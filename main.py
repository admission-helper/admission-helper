#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import random
from student import full_info
from memo import *
from commands import *

from secret import token

from chat_bot import model, start

# login, password='login','password'
# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()

vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

keyboard_history = []
text_history = ["Вы и так в самом низу"]
faculty = ["Ты не выбрал факультет ау"]
level = ["Ты не выбрал уровень обучения ау"]
direction = ["Ты не выбрал направление ау"]
saved_name = ""
name_field = False
answer_field = False
is_saved = False


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    response = response.lower()

    if response == 'старт':
        keyboard = start_button(keyboard, keyboard_history)

    elif response == "назад":
        keyboard = return_keyboard(keyboard_history)

    elif response == "общая информация":
        text_history.append("старт")
        keyboard = subscribe(keyboard, keyboard_history)

    elif response == "информация о вузе":
        text_history.append("общая информация")
        keyboard = info(keyboard, keyboard_history)

    elif response == "контакты":
        text_history.append("общая информация")
        keyboard = contacts(keyboard, keyboard_history)

    elif response == 'информация по факультетам':
        text_history.append("старт")
        keyboard = f_cks(keyboard, keyboard_history)

    elif response == "юридический":
        text_history.append("информация по факультетам")
        faculty.append("юридический")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "экономический":
        faculty.append("экономический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "ивт":
        faculty.append("ивт")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "математический":
        faculty.append("математический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "физический":
        faculty.append("физический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "биологии и экологии":
        faculty.append("биологии и экологии")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "психологический":
        faculty.append("психологический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "филологии и коммуникации":
        faculty.append("филологии и коммуникации")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "институт иностранных языков":
        faculty.append("институт иностранных языков")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "фспн":
        faculty.append("фспн")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "исторический":
        faculty.append("исторический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "университетский колледж":
        faculty.append("университетский колледж")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard, keyboard_history)

    elif response == "как поступить?":
        text_history.append(faculty[-1])
        keyboard = levels(keyboard, keyboard_history)

    elif response == "бакалавриат и специалитет":
        text_history.append("бакалавриат и специалитет")
        level.append("бакалавриат и специалитет")
        if faculty[-1] == "математический":
            keyboard = math_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "ивт":
            keyboard = it_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "физический":
            keyboard = physical_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "биологии и экологии":
            keyboard = biology_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "психологии":
            keyboard = psycological_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "экономический":
            keyboard = economic_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "фспн":
            keyboard = social_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "юридический":
            keyboard = law_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "филологии и коммуникации":
            keyboard = feel_f_ck_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "исторический":
            keyboard = historical_bachelor(keyboard, keyboard_history)

    elif response == "магистратура":
        text_history.append("магистратура")
        level.append("магистратура")
        if faculty[-1] == "математический":
            keyboard = math_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "ивт":
            keyboard = it_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "физический":
            keyboard = physical_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "биологии и экологии":
            keyboard = biology_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "психологии":
            keyboard = psycological_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "экономический":
            keyboard = economic_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "фспн":
            keyboard = social_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "юридический":
            keyboard = law_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "филологии и коммуникации":
            keyboard = feel_f_ck_bachelor(keyboard, keyboard_history)
        elif faculty[-1] == "исторический":
            keyboard = historical_bachelor(keyboard, keyboard_history)

    elif response == "аспирантура":
        text_history.append("аспирантура")
        level.append("аспирантура")
        if faculty[-1] == "математический":
            keyboard = math_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "ивт":
            keyboard = it_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "физический":
            keyboard = physical_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "биологии и экологии":
            keyboard = biology_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "психологии":
            keyboard = psycological_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "экономический":
            keyboard = economic_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "фспн":
            keyboard = social_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "юридический":
            keyboard = law_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "филологии и коммуникации":
            keyboard = feel_f_ck_graduate(keyboard, keyboard_history)
        elif faculty[-1] == "исторический":
            keyboard = historical_graduate(keyboard, keyboard_history)

    elif response == "способы подачи документов":
        text_history.append("как поступить?")
        keyboard = variants(keyboard, keyboard_history)

    elif response == "где трудиться?":
        text_history.append(faculty[-1])
        keyboard = back(keyboard, keyboard_history)

    elif response == "в электронной форме":
        keyboard = back(keyboard, keyboard_history)

    elif response == "по почте":
        keyboard = back(keyboard, keyboard_history)

    elif response == "контакты факультета":
        keyboard = back(keyboard, keyboard_history)

    elif response == "направления":
        text_history.append(faculty[-1])
        keyboard = levels(keyboard, keyboard_history)

    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response == 'узнать свой рейтинг':
        text_history.append("старт")
        keyboard = change(keyboard, keyboard_history)

    elif response == "да" or response == "нет":
        keyboard = back(keyboard, keyboard_history)

    #elif full_info(response) != 'Имя нет в списке':
        #keyboard = save(keyboard, keyboard_history)

    elif response == 'закрыть':
        return keyboard.get_empty_keyboard()

    else:
        return keyboard.get_empty_keyboard()

    # print(faculty)

    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

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

            elif response == "назад":
                send_message(vk_session, 'user_id', event.user_id, message=text_history[-1], keyboard=keyboard)

            elif response == "старт":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды:', keyboard=keyboard)

            elif response == "общая информация":
                send_message(vk_session, 'user_id', event.user_id, message= 'Общая информация:', keyboard=keyboard)

            elif response == "информация о вузе":
                send_message(vk_session, 'user_id', event.user_id, message='Информация о вузе:', keyboard=keyboard)

            elif response == "контакты":
                send_message(vk_session, 'user_id', event.user_id, message='Контакты:', keyboard=keyboard)

            elif response == "история вуза":
                send_message(vk_session, 'user_id', event.user_id, message='Появился.')

            elif response == "учёный совет":
                send_message(vk_session, 'user_id', event.user_id, message='Илья Апальков и остальные замы')

            elif response == "основные документы":
                send_message(vk_session, 'user_id', event.user_id, message='Методичка Кубышкина')

            elif response == "контакты вуза":
                send_message(vk_session, 'user_id', event.user_id, message="Адрес: 150003, г. Ярославль, ул. Советская, д. 14\n"
                                                                           "График работы: пн, вт, ср, чт: 9.00-12.00, 14.00-17.00, пт: 9.00-12.00, 14.00-16.00.\n"
                                                                           "Телефон: +7 (4852) 79-77-94\n"
                                                                           "e-mail: rectorat@uniyar.ac.ru\n"
                                                                           "Группа ВКонтакте: https://vk.com/yaroslavl_state_university\n"
                                                                           "Инстаграм: https://www.instagram.com/demid_yargu/")

            elif response == "контакты приёмной комиссии":
                send_message(vk_session, 'user_id', event.user_id, message="Адрес: 150000, г. Ярославль, ул.Кирова 8/10, каб. 102\n"
                                                                           "График работы: понедельник - пятница: 09:00 - 16:00; суббота: 10:00 - 13:00\n"
                                                                           "Телефон: +7(4852)30-32-10, 78-85-33\n"
                                                                           "e-mail: abitur@uniyar.ac.ru\n"
                                                                           "Группа ВКонтакте: https://vk.com/uniyar_abitur")

            elif response == "контакты приёмной комиссии (для иностранных граждан)":
                send_message(vk_session, 'user_id', event.user_id, message="Адрес: 150000, г. Ярославль, ул.Кирова 8/10, каб. 102\n"
                                                                           "График работы: понедельник - пятница: 09:00 - 16:00; суббота: 10:00 - 13:00\n"
                                                                           "Телефон: +7 (4852) 79-77-45, 79-77-46\n"
                                                                           "e-mail: depint@uniyar.ac.ru\n"
                                                                           "Группа ВКонтакте: https://vk.com/uniyar_abitur")

            elif response == "информация по факультетам":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите факультет:', keyboard=keyboard)

            elif response == "бакалавриат и специалитет":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите направление:", keyboard=keyboard)

            elif response == "магистратура":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите направление:", keyboard=keyboard)

            elif response == "аспирантура":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите направление:", keyboard=keyboard)

            elif response == "прикладная математика и информатика":
                if faculty[-1] == "математический":
                    if level[-1] == "бакалавриат и специалитет":
                        send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("01.03.02")) + "\n"
                                                                                   "Проходной балл: " + str(score("01.03.02")) + "\n"
                                                                                   "Стоимость обучения: " + str(price("01.03.02")) + "\n"
                                                                                   "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("01.03.02")))
                    elif level[-1] == "магистратура":
                        send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("01.04.02")) + "\n"
                                                                                   "КЦП бюджет: " + str(numbers1_undergraduate("01.04.02")) + "\n"
                                                                                   "КЦП целевые места: " + str(numbers2_undergraduate("01.04.02")) + "\n"
                                                                                   "КЦП внебюджет: " + str(numbers3_undergraduate("01.04.02")) + "\n"
                                                                                   "Вступительное испытание: " + str(exams_undergraduate("01.04.02")))
                    else:
                        send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                                   "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
                elif faculty[-1] == "ивт":
                    if level[-1] == "бакалавриат и специалитет":
                        send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("01.03.02")) + "\n"
                                                                                   "Проходной балл: " + str(score("01.03.02")) + "\n"
                                                                                   "Стоимость обучения: " + str(price("01.03.02")) + "\n"
                                                                                   "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("01.03.02")))
                    elif level[-1] == "магистратура":
                        send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("01.04.02")) + "\n"
                                                                                   "КЦП бюджет: " + str(numbers1_undergraduate("01.04.02")) + "\n"
                                                                                   "КЦП целевые места: " + str(numbers2_undergraduate("01.04.02")) + "\n"
                                                                                   "КЦП внебюджет: " + str(numbers3_undergraduate("01.04.02")) + "\n"
                                                                                   "Вступительное испытание: " + str(exams_undergraduate("01.04.02")))
                    else:
                        send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                                   "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал факультет.\n"
                                                                               "Чтобы выбрать факультет выбери: Информация по факультетам -> *Свой факультет*")
            elif response == "математика и компьютерные науки":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("02.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("02.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("02.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("02.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("02.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("02.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("02.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("02.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("02.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "информационная безопасность":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("10.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("10.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("10.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("10.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("10.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("10.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("10.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("10.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("10.04.01")))
                elif level[-1] == "аспирантура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("10.06.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_graduate("10.06.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_graduate("10.06.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_graduate("10.06.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_graduate("10.06.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "компьютерная безопасность":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("10.05.01")) + "\n"
                                                                           "Проходной балл: " + str(score("10.05.01")) + "\n"
                                                                           "Стоимость обучения: " + str(price("10.05.01")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("10.05.01")))
            elif response == "математика и механика":
                if faculty[-1] == "математический":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("01.06.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_graduate("01.06.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_graduate("01.06.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_graduate("01.06.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_graduate("01.06.01")))
                elif faculty[-1] == "ивт":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("01.06.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_graduate("01.06.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_graduate("01.06.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_graduate("01.06.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_graduate("01.06.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал факультет.\n"
                                                                               "Чтобы выбрать факультет выбери: Информация по факультетам -> *Свой факультет*")
            elif response == "информатика и вычислительная техника":
                if faculty[-1] == "математический":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("09.06.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_graduate("09.06.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_graduate("09.06.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_graduate("09.06.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_graduate("09.06.01")))
                elif faculty[-1] == "ивт":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("09.06.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_graduate("09.06.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_graduate("09.06.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_graduate("09.06.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_graduate("09.06.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал факультет.\n"
                                                                               "Чтобы выбрать факультет выбери: Информация по факультетам -> *Свой факультет*")
            elif response == "информационная безопасность":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("10.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("10.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("10.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("10.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("10.06.01")))
            elif response == "фундаментальная информатика и информационные технологии":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("02.03.02")) + "\n"
                                                                               "Проходной балл: " + str(score("02.03.02")) + "\n"
                                                                               "Стоимость обучения: " + str(price("02.03.02")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("02.03.02")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("02.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("02.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("02.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("02.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("02.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "прикладная информатика в экономике":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("09.03.03")) + "\n"
                                                                           "Проходной балл: " + str(score("09.03.03")) + "\n"
                                                                           "Стоимость обучения: " + str(price("09.03.03")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("09.03.03")))
            elif response == "прикладная информатика":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("09.04.03")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_undergraduate("09.04.03")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_undergraduate("09.04.03")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_undergraduate("09.04.03")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_undergraduate("09.04.03")))
            elif response == "компьютерные и информационные науки":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("02.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("02.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("02.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("02.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("02.06.01")))
            elif response == "физика":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("03.03.02")) + "\n"
                                                                               "Проходной балл: " + str(score("03.03.02")) + "\n"
                                                                               "Стоимость обучения: " + str(price("03.03.02")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("03.03.02")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("03.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("03.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("03.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("03.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("03.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "радиофизика":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("03.03.03")) + "\n"
                                                                               "Проходной балл: " + str(score("03.03.03")) + "\n"
                                                                               "Стоимость обучения: " + str(price("03.03.03")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("03.03.03")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("03.04.03")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("03.04.03")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("03.04.03")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("03.04.03")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("03.04.03")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "радиотехника":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("11.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("11.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("11.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("11.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("11.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("11.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("11.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("11.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("11.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "инфокоммуникационные технологии и системы связи":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("11.03.02")) + "\n"
                                                                               "Проходной балл: " + str(score("11.03.02")) + "\n"
                                                                               "Стоимость обучения: " + str(price("11.03.02")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("11.03.02")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("11.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("11.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("11.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("11.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("11.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "электроника и наноэлектроника":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("11.03.04")) + "\n"
                                                                               "Проходной балл: " + str(score("11.03.04")) + "\n"
                                                                               "Стоимость обучения: " + str(price("11.03.04")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("11.03.04")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("11.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("11.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("11.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("11.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("11.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "физика и астрономия":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("03.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("03.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("03.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("03.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("03.06.01")))
            elif response == "электроника, радиоэлектроника и системы связи":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("11.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("11.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("11.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("11.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("11.06.01")))
            elif response == "химия":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("04.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("04.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("04.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("04.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("04.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("04.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("04.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("04.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("04.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "биология":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("06.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("06.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("06.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("06.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("06.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("06.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("06.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("06.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("06.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "экология и природопользование":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("05.03.06")) + "\n"
                                                                               "Проходной балл: " + str(score("05.03.06")) + "\n"
                                                                               "Стоимость обучения: " + str(price("05.03.06")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("05.03.06")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("05.04.06")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("05.04.06")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("05.04.06")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("05.04.06")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("05.04.06")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "химические науки":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("04.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("04.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("04.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("04.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("04.06.01")))
            elif response == "биологические науки":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("06.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("06.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("06.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("06.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("06.06.01")))
            elif response == "психология":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("37.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("37.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("37.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("37.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("37.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("37.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("37.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("37.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("37.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "психолого-педагогическое образование":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("44.04.02")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_undergraduate("44.04.02")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_undergraduate("44.04.02")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_undergraduate("44.04.02")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_undergraduate("44.04.02")))
            elif response == "психологические науки":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("37.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("37.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("37.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("37.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("37.06.01")))
            elif response == "экономика (бух. учёт, анализ и аудит)":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("38.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("38.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("38.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("38.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("37.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("38.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("38.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "экономика (мировая экономика и международный бизнес)":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("38.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("38.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("38.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("38.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("38.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("38.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "экономика (финансы и кредит)":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("38.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("38.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("38.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("38.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("38.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("38.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("38.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "менеджмент":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("38.03.02")) + "\n"
                                                                               "Проходной балл: " + str(score("38.03.02")) + "\n"
                                                                               "Стоимость обучения: " + str(price("38.03.02")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("38.03.02")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("38.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("38.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("38.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("38.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("38.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "государственное и муниципальное управление":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("38.03.04")) + "\n"
                                                                               "Проходной балл: " + str(score("38.03.04")) + "\n"
                                                                               "Стоимость обучения: " + str(price("38.03.04")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("38.03.04")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("38.04.04")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("38.04.04")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("38.04.04")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("38.04.04")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("38.04.04")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "Экономика (Экономическая теория)":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("38.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("38.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("38.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("38.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("38.06.01")))
            elif response == "Экономика (Экономика и управление народным хозяйством)":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("38.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("38.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("38.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("38.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("38.06.01")))
            elif response == "Экономика (Финансы, денежное обращение и кредит)":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("38.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("38.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("38.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("38.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("38.06.01")))
            elif response == "Экономика (Бухгалтерский учёт, статистика)":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("38.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("38.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("38.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("38.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("38.06.01")))
            elif response == "Экономика (Мировая экономика)":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("38.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("38.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("38.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("38.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("38.06.01")))
            elif response == "социология":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("39.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("39.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("39.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("39.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("39.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("39.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("39.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("39.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("39.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "социальная работа":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("39.03.02")) + "\n"
                                                                               "Проходной балл: " + str(score("39.03.02")) + "\n"
                                                                               "Стоимость обучения: " + str(price("39.03.02")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("39.03.02")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("39.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("39.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("39.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("39.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("39.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "социальная работа (заочная)":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("39.03.02")) + "\n"
                                                                           "Проходной балл: " + str(score("39.03.02")) + "\n"
                                                                           "Стоимость обучения: " + str(price("39.03.02")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("39.03.02")))
            elif response == "организация работы с молодёжью":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("39.03.03")) + "\n"
                                                                               "Проходной балл: " + str(score("39.03.03")) + "\n"
                                                                               "Стоимость обучения: " + str(price("39.03.03")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("39.03.03")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("39.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("39.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("39.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("39.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("39.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "организация работы с молодёжью (заочная)":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("39.03.03")) + "\n"
                                                                           "Проходной балл: " + str(score("39.03.03")) + "\n"
                                                                           "Стоимость обучения: " + str(price("39.03.03")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("39.03.03")))
            elif response == "политология":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("41.03.03")) + "\n"
                                                                               "Проходной балл: " + str(score("41.03.06")) + "\n"
                                                                               "Стоимость обучения: " + str(price("41.03.06")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("41.03.06")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("41.04.04")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("41.04.04")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("41.04.04")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("41.04.04")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("41.04.04")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "публичная политика и социальные науки":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("41.03.06")) + "\n"
                                                                           "Проходной балл: " + str(score("41.03.06")) + "\n"
                                                                           "Стоимость обучения: " + str(price("41.03.06")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("41.03.06")))
            elif response == "юриспруденция":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("40.03.01")) + "\n"
                                                                           "Проходной балл: " + str(score("40.03.01")) + "\n"
                                                                           "Стоимость обучения: " + str(price("40.03.01")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("40.03.01")))
            elif response == "юриспруденция (очно-заочная)":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("40.03.01")) + "\n"
                                                                           "Проходной балл: " + str(score("40.03.01")) + "\n"
                                                                           "Стоимость обучения: " + str(price("40.03.01")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("40.03.01")))
            elif response == "прикладная филология":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("45.03.01")) + "\n"
                                                                           "Проходной балл: " + str(score("45.03.01")) + "\n"
                                                                           "Стоимость обучения: " + str(price("45.03.01")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("45.03.01")))
            elif response == "зарубежная филология":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("45.03.01")) + "\n"
                                                                           "Проходной балл: " + str(score("45.03.01")) + "\n"
                                                                           "Стоимость обучения: " + str(price("45.03.01")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("45.03.01")))
            elif response == "реклама и связи с общественностью":
                send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("42.03.01")) + "\n"
                                                                           "Проходной балл: " + str(score("42.03.01")) + "\n"
                                                                           "Стоимость обучения: " + str(price("42.03.01")) + "\n"
                                                                           "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("42.03.01")))
            elif response == "туризм":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("43.03.02")) + "\n"
                                                                               "Проходной балл: " + str(score("43.03.02")) + "\n"
                                                                               "Стоимость обучения: " + str(price("43.03.02")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("43.03.02")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("43.04.02")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("43.04.02")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("43.04.02")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("43.04.02")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("43.04.02")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "история":
                if level[-1] == "бакалавриат и специалитет":
                    send_message(vk_session, 'user_id', event.user_id, message="Количество бюджетных мест: " + str(count("46.03.01")) + "\n"
                                                                               "Проходной балл: " + str(score("46.03.01")) + "\n"
                                                                               "Стоимость обучения: " + str(price("46.03.01")) + "\n"
                                                                               "Вступительные испытания (ЕГЭ): " + str(exams_bachelor("46.03.01")))
                elif level[-1] == "магистратура":
                    send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_undergraduate("46.04.01")) + "\n"
                                                                               "КЦП бюджет: " + str(numbers1_undergraduate("46.04.01")) + "\n"
                                                                               "КЦП целевые места: " + str(numbers2_undergraduate("46.04.01")) + "\n"
                                                                               "КЦП внебюджет: " + str(numbers3_undergraduate("46.04.01")) + "\n"
                                                                               "Вступительное испытание: " + str(exams_undergraduate("46.04.01")))
                else:
                    send_message(vk_session, 'user_id', event.user_id, message="Ты не выбрал уровень обучения.\n"
                                                                               "Чтобы выбрать уровень обучения выбери: Информация по факультетам -> *Свой факультет* -> Как поступить?")
            elif response == "исторические науки и археология":
                send_message(vk_session, 'user_id', event.user_id, message="Наименование направленности: " + str(focuses_graduate("46.06.01")) + "\n"
                                                                           "КЦП бюджет: " + str(numbers1_graduate("46.06.01")) + "\n"
                                                                           "КЦП целевые места: " + str(numbers2_graduate("46.06.01")) + "\n"
                                                                           "КЦП внебюджет: " + str(numbers3_graduate("46.06.01")) + "\n"
                                                                           "Вступительное испытание: " + str(exams_graduate("46.06.01")))
            elif response == "лично":
                send_message(vk_session, 'user_id', event.user_id, message= "Приемная комиссия работает по адресу: Ярославль, ул. Кирова, д. 8/10.", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "   с понедельника по пятницу с 9.00 до 16.00,", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "   в субботу — с 10.00 до 13.00 (воскресенье — выходной день).", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Телефоны приемной комиссии: (4852) 30-32-10, 31-43-73.", keyboard=keyboard)

            elif response == "в электронной форме":
                send_message(vk_session, 'user_id', event.user_id, message= "http://online.priem.uniyar.ac.ru", keyboard=keyboard)

            elif response == "по почте":
                send_message(vk_session, 'user_id', event.user_id, message= "150000, Ярославль, ул. Кирова, д. 8/10", keyboard=keyboard)

            elif response == "где трудиться?":
                send_message(vk_session, 'user_id', event.user_id, message= "СВАРЩИК СВАРЩИК ПАРЕНЬ РАБОТЯЩИЙ", keyboard=keyboard)

            elif response == "контакты факультета":
                if faculty[-1] == "математический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Адрес факультета: 150008, г. Ярославль, ул. Союзная, 144", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Телефон деканата: +7 4852 78-85-91", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Телефон для справок по вопросам поступления : +7 964 482 6310", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "WhatsApp : +7 964 482 6310", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "E-mail по вопросам поступления: kaphedra@mail.ru", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Группа для абитуриентов ВКонтакте: https://vk.com/math_yargu", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Группа для абитуриентов ВКонтакте: https://vk.com/math_yargu", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Наш инстаграм: https://www.instagram.com/math_yargu/", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Страница школы при математическом факультете: https://math.uniyar.ac.ru/for-scholars", keyboard=keyboard)
                elif faculty[-1] == "ивт":
                    send_message(vk_session, 'user_id', event.user_id, message= "Телефон: +7 (4852) 78-85-86", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "EMail: icsdep@uniyar.ac.ru", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Адрес: 150007, Ярославль, ул. Союзная, 144, 7 корпус", keyboard=keyboard)
                elif faculty[-1] == "физический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Телефон: +7 (4852) 30-32-62", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "E-mail: physdep@uniyar.ac.ru", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Адрес: 150007, Ярославль, ул. Кирова, 8/10, 2-й корпус", keyboard=keyboard)
                elif faculty[-1] == "экономический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Адрес: 150000, г. Ярославль, ул. Комсомольская 3 ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Декан факультета:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Парфёнова Людмила Борисовна, д.э.н., профессор", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Телефон (раб.): (4852) 78-86-14", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   E-mail: decan@econom.uniyar.ac.ru", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Методист очной формы обучения:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Каримова Галина Васильевна", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Телефон (раб.): (4852) 78-86-13", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Методист очно-заочной и заочной форм обучения:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Жулябина Светлана Вячеславовна", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Телефон (раб.): (4852) 78-86-20", keyboard=keyboard)
                elif faculty[-1] == "фспн":
                    send_message(vk_session, 'user_id', event.user_id, message= "Адрес: 150000, г. Ярославль, ул. Советская, 10", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Телефон: +7 (4852) 78-85-21", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "EMail: fspn@uniyar.ac.ru", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Телефон (раб.): (4852) 78-86-14", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   E-mail: decan@econom.uniyar.ac.ru", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Методист очной формы обучения:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Каримова Галина Васильевна", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Телефон (раб.): (4852) 78-86-13", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Методист очно-заочной и заочной форм обучения:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Жулябина Светлана Вячеславовна", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Телефон (раб.): (4852) 78-86-20", keyboard=keyboard)

            elif response == "вопрос":
                send_message(vk_session, 'user_id', event.user_id, message= "Зайдайте мне вопрос. Я отвечу в течение дня.", keyboard=keyboard)

            elif response == "узнать свой рейтинг":
                if is_saved:
                    send_message(vk_session, 'user_id', event.user_id, message=full_info(saved_name), keyboard=keyboard)
                else:
                    send_message(vk_session, 'user_id', event.user_id, message='Введите ваше имя:')
                    name_field = True

            elif name_field == True:
                send_message(vk_session, 'user_id', event.user_id, message=full_info(response))
                if full_info(response) != 'Имя не в списке':
                    send_message(vk_session, 'user_id', event.user_id, message='Сохранить имя?', keyboard=keyboard)
                saved_name = response
                name_field = False
                answer_field = True

            elif answer_field == True:
                if response == "да":
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше имя сохранено', keyboard=keyboard)
                    is_saved = True
                    answer_field = False
                elif response == "нет":
                    send_message(vk_session, 'user_id', event.user_id, message='Ладно.', keyboard=keyboard)
                    answer_field = False

            elif response == "изменить":
                send_message(vk_session, 'user_id', event.user_id, message='Введите ваше имя:')
                name_field = True

            elif response == "специальности":
                send_message(vk_session, 'user_id', event.user_id, message= 'Специальности:', keyboard=keyboard)

            elif response == "экономический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Экономический:', keyboard=keyboard)

            elif response == "юридический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Юридический:', keyboard=keyboard)

            elif response == "ивт":
                send_message(vk_session, 'user_id', event.user_id, message= 'Факультет информатики и вычислительной техники:', keyboard=keyboard)

            elif response == "математический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Математический:', keyboard=keyboard)

            elif response == "физический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Физический:', keyboard=keyboard)

            elif response == "биологии и экологии":
                send_message(vk_session, 'user_id', event.user_id, message= 'Факультет биологии и экологии:', keyboard=keyboard)

            elif response == "психологический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Психологический:', keyboard=keyboard)

            elif response == "филологический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Филологический:', keyboard=keyboard)

            elif response == "институт ин. языков":
                send_message(vk_session, 'user_id', event.user_id, message= 'Институт иностранных языков:', keyboard=keyboard)

            elif response == "фспн":
                send_message(vk_session, 'user_id', event.user_id, message= 'Факультет социально политических наук:', keyboard=keyboard)

            elif response == "исторический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Исторический:', keyboard=keyboard)

            elif response == "университетский колледж":
                send_message(vk_session, 'user_id', event.user_id, message= 'Университетский колледж:', keyboard=keyboard)

            elif response == "как поступить?":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите уровень обучения:', keyboard=keyboard)

            elif response == "направления":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите уровень обучения', keyboard=keyboard)

            elif response == "выберите направление":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите направление:', keyboard=keyboard)

            elif response == 'команды':
                send_message(vk_session, 'user_id', event.user_id, message='Список команд бота: \n \n 1)Команда1 \n 2)Команда2')

            elif response == 'закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)

            elif response == "Можно ли оплачивать учёбу не по семестру, а по месячно?":
                send_message(vk_session, 'user_id', event.user_id, message= full_info('Дык Фам'))
            else:
                send_message(vk_session, 'user_id', event.user_id, message= start(response, model))