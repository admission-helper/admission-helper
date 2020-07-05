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
direction = ["Ты не выбрал направление ау"]

# model = get_model()

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    response = response.lower()

    if response == 'старт':
        keyboard = start_button(keyboard, keyboard_history)

    elif response == "назад":
        keyboard = return_keyboard(keyboard, keyboard_history)

    elif response == "приёмная комиссия":
        text_history.append("старт")
        keyboard = sc(keyboard, keyboard_history)

    elif response == "информация для абитуриентов":
        text_history.append("старт")
        faculty.append("информация для абитуриентов")
        keyboard = level(keyboard, keyboard_history)

    elif response == "бакалавриат и специалитет":
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == "магистратура":
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == "аспирантура":
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == "среднее профессиональное образование":
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == "контакты приёмной комиссии":
        text_history.append("старт")
        keyboard = sc_contacts(keyboard, keyboard_history)

    elif response == 'узнать свой рейтинг':
        text_history.append("старт")

    elif response == 'адрес':
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == 'телефон':
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == 'email':
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == 'skype':
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == 'телефон (для иностранных граждан)':
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == 'адрес (для иностранных граждан)':
        text_history.append("старт")
        keyboard = back(keyboard, keyboard_history)

    elif response == 'контакты приёмной комиссии':
        text_history.append("старт")
        keyboard = sc_contacts(keyboard, keyboard_history)

    elif response == 'информация по факультетам':
        text_history.append("старт")
        keyboard = faculties(keyboard, keyboard_history)

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

    elif response == "филологический":
        faculty.append("филологический")
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

    elif response == "количество бюджетных мест":
        text_history.append(direction[-1])
        keyboard = back(keyboard, keyboard_history)

    elif response == "проходной балл":
        text_history.append(direction[-1])
        keyboard = back(keyboard, keyboard_history)

    elif response == "стоимость обучения":
        text_history.append(direction[-1])
        keyboard = back(keyboard, keyboard_history)

    elif response == "как поступить?":
        text_history.append(faculty[-1])
        keyboard = how(keyboard, keyboard_history)

    elif response == "выберите направление":
        text_history.append("как поступить?")
        if faculty[-1] == "экономический":
            keyboard = economic_directions(keyboard, keyboard_history)
        elif faculty[-1] == "юридический":
            keyboard = law_directions(keyboard, keyboard_history)
        elif faculty[-1] == "исторический":
            keyboard = history_directions(keyboard, keyboard_history)
        elif faculty[-1] == "фспн":
            keyboard = social_directions(keyboard, keyboard_history)
        elif faculty[-1] == "ивт":
            keyboard = it_directions(keyboard, keyboard_history)
        elif faculty[-1] == "математический":
            keyboard = math_directions(keyboard, keyboard_history)
        elif faculty[-1] == "физический":
            keyboard = physical_directions(keyboard, keyboard_history)
        elif faculty[-1] == "биологии и экологии":
            keyboard = biology_directions(keyboard, keyboard_history)
        elif faculty[-1] == "психологии":
            keyboard = psycology_directions(keyboard, keyboard_history)
        elif faculty[-1] == "филологии и коммуникации":
            keyboard = feel_f_ck_directions(keyboard, keyboard_history)
        else:
            keyboard = back(keyboard, keyboard_history)

    elif response == "прикладная математика и информатика":
        text_history.append("выберите направления")
        direction.append("прикладная математика и информатика")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "математика и компьютерные науки":
        text_history.append("выберите направления")
        direction.append("математика и компьютерные науки")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "информационная безопасность":
        text_history.append("выберите направления")
        direction.append("информационная безопасность")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "компьютерная безопасность":
        text_history.append("выберите направления")
        direction.append("компьютерная безопасность")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "прикладная математика и информатика":
        text_history.append("выберите направления")
        direction.append("прикладная математика и информатика")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "фундаментальная информатика и информационные технологии":
        text_history.append("выберите направления")
        direction.append("фундаментальная информатика и информационные технологии")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "прикладная информаиика в экономике":
        text_history.append("выберите направления")
        direction.append("прикладная информаиика в экономике")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "физика":
        text_history.append("выберите направления")
        direction.append("физика")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "радиофизика":
        text_history.append("выберите направления")
        direction.append("радиофизика")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "радиотехника":
        text_history.append("выберите направления")
        direction.append("радиотехника")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "инфокоммуникационные технологии и системы связи":
        text_history.append("выберите направления")
        direction.append("инфокоммуникационные технологии и системы связи")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "электроника и наноэлектроника":
        text_history.append("выберите направления")
        direction.append("электроника и наноэлектроника")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "химия":
        text_history.append("выберите направления")
        direction.append("химия")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "биология":
        text_history.append("выберите направления")
        direction.append("биология")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "экология и природопользование":
        text_history.append("выберите направления")
        direction.append("экология и природопользование")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "психология":
        text_history.append("выберите направления")
        direction.append("психология")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "экономика (бух. учёт, анализ и аудит)":
        text_history.append("выберите направления")
        direction.append("экономика (бух. учёт, анализ и аудит)")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "экономика (мировая экономика и международный бизнес)":
        text_history.append("выберите направления")
        direction.append("экономика (мировая экономика и международный бизнес)")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "экономика (финансы и кредит)":
        text_history.append("выберите направления")
        direction.append("экономика (финансы и кредит)")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "менеджмент":
        text_history.append("выберите направления")
        direction.append("менеджмент")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "государственное и муниципальное управление":
        text_history.append("выберите направления")
        direction.append("государственное и муниципальное управление")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "социология":
        text_history.append("выберите направления")
        direction.append("социология")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "социальная работа":
        text_history.append("выберите направления")
        direction.append("социальная работа")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "социальная работа (заочная)":
        text_history.append("выберите направления")
        direction.append("социальная работа (заочная)")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "организация работы с молодёжью":
        text_history.append("выберите направления")
        direction.append("организация работы с молодёжью")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "организация работы с молодёжью (заочная)":
        text_history.append("выберите направления")
        direction.append("организация работы с молодёжью (заочная)")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "политология":
        text_history.append("выберите направления")
        direction.append("политология")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "публичная политика и социальные науки":
        text_history.append("выберите направления")
        direction.append("публичная политика и социальные науки")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "юриспруденция":
        text_history.append("выберите направления")
        direction.append("юриспруденция")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "юриспруденция (очно-заочная)":
        text_history.append("выберите направления")
        direction.append("юриспруденция (очно-заочная)")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "прикладная филология":
        text_history.append("выберите направления")
        direction.append("прикладная филология")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "зарубежная филология":
        text_history.append("выберите направления")
        direction.append("зарубежная филология")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "реклама и связи с общественностью":
        text_history.append("выберите направления")
        direction.append("реклама и связи с общественностью")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "туризм":
        text_history.append("выберите направления")
        direction.append("туризм")
        keyboard = direction_menu(keyboard, keyboard_history)
    elif response == "история":
        text_history.append("выберите направления")
        direction.append("история")
        keyboard = direction_menu(keyboard, keyboard_history)

    elif response == "способы подачи документов":
        text_history.append("как поступить?")
        keyboard = variants(keyboard, keyboard_history)

    elif response == "лично":
        keyboard = back(keyboard, keyboard_history)

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
        keyboard = level(keyboard, keyboard_history)

    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        #print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    else:
        return keyboard.get_empty_keyboard()

    # print(faculty)

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

            elif response == "назад":
                send_message(vk_session, 'user_id', event.user_id, message= text_history[-1], keyboard=keyboard)

            elif response == "старт":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды:', keyboard=keyboard)

            elif response == "бакалавриат и специалитет":
                if faculty == "информация для абитуриентов":
                    send_message(vk_session, 'user_id', event.user_id, message= "Количество мест для приема по программам бакалавриата и специалитета 2020 с выделением мест по особому праву и целевых мест", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Количество мест для приема по программам бакалавриата для обучения в ускоренные сроки в 2020 году (на базе среднего профессионального или высшего образования)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация для поступающих на целевое обучение", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Проект расписания вступительных испытаний (для поступающих не по результатам ЕГЭ)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Список документов при подаче заявления 2020", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Согласие на обработку персональных данных", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Памятка для абитуриента (направления, стоимость, проходные баллы 2019)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Стоимость обучения в 2020-2021 учебном году", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Положение о скидках по оплате обучения 2019", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "ПРАВИЛА ПРИЕМА ПО ПРОГРАММАМ БАКАЛАВРИАТА И СПЕЦИАЛИТЕТА 2020/2021", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Сроки проведения приема", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Учет индивидуальных достижений", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Программы вступительных испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Перечень вступительных  испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Минимальное количество баллов и шкала оценивания", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Формы проведения вступительных испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Правила подачи и рассмотрения апелляций", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Особенности проведения вступительных испытаний для лиц с ограниченными возможностями здоровья", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация об особых правах и преимуществах", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Образцы договоров об оказании платных услуг", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Подача документов в электронной форме", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Места приема документов, почтовые и электронные адреса для направления документов", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация об общежитии", keyboard=keyboard)
                elif faculty == "экономический":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Экономика', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Менеджмент', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Государственное и минуципальное направление', keyboard=keyboard)
                elif faculty == "юридический":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Юриспруденция', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Юриспруденция (очно-заочный)', keyboard=keyboard)
                elif faculty == "исторический":
                    send_message(vk_session, 'user_id', event.user_id, message= 'История', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Туризм', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Реклама и связи с общественностью', keyboard=keyboard)
                elif faculty == "фспн":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Социальная', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Социальная работа', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Политология', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Публичная политика и социальные науки', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Организация работы с молодежью', keyboard=keyboard)
                elif faculty == "ивт":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Прикладная математика и информатика', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Фундаментальная информатика и информационные технологии', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Прикладная информатика', keyboard=keyboard)
                elif faculty == "математический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Математика и компьютерные науки", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Прикладная математика и информатика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информационная безопасность", keyboard=keyboard)
                elif faculty == "физический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Физика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Радиофизика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Радиотехника", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Инфокоммуникационные технологии и системы связи ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Электроника и наноэлектроника ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Инфокоммуникационные технологии и системы связи (заочная форма)", keyboard=keyboard)
                elif faculty == "биологии и экологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "Биология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Химия", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Экология и природопользование", keyboard=keyboard)
                elif faculty == "психологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "Основными направлениями научной работы на факультете являются:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Метакогнитивная психология деятельности", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология практического мышления и опыта", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология творческого профессионального мышления ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Социально-психологические закономерности функционирования коллективного субъекта профессиональной деятельности", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Методология, теория и практика профессиональной деятельности психолога-консультанта", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Интегративная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология вузовской адаптации", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Спортивная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Социальное познание в международных отношениях на примере коллективного субъекта (государства)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Организационная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Когнитивная психология и нейронаука", keyboard=keyboard)
                elif faculty == "филологии и коммуникации":
                    send_message(vk_session, 'user_id', event.user_id, message= "Прикладная филология (русский язык)", keyboard=keyboard)
                elif faculty == "институт иностранных языков":
                    send_message(vk_session, 'user_id', event.user_id, message= "Зарубежная филология (английский язык и литература)", keyboard=keyboard)

            elif response == "магистратура":
                if faculty == "информация для абитуриентов":
                    send_message(vk_session, 'user_id', event.user_id, message= "Контрольные цифры приема по программам магистратуры 2020", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Проект расписания вступительных испытаний 2020", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация для поступающих на целевое обучение", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Проект расписания вступительных испытаний (для поступающих не по результатам ЕГЭ)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Список документов при подаче заявления 2020", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Согласие на обработку персональных данных", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Стоимость обучения в 2020-2021 учебном году", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Положение о скидках по оплате обучения 2019", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "ПРАВИЛА ПРИЕМА ПО ПРОГРАММАМ МАГИСТРАТУРЫ 2020/2021", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Сроки проведения приема", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Учет индивидуальных достижений", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Программы вступительных испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Перечень вступительных  испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Минимальное количество баллов и шкала оценивания", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Формы проведения вступительных испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Правила подачи и рассмотрения апелляций", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Особенности проведения вступительных испытаний для лиц с ограниченными возможностями здоровья", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация об особых правах и преимуществах", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Образцы договоров об оказании платных услуг", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Подача документов в электронной форме", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Места приема документов, почтовые и электронные адреса для направления документов", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация об общежитии", keyboard=keyboard)
                elif faculty == "экономический":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Экономика', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Менеджмент', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Государственное и минуципальное направление', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Финансы и кредит', keyboard=keyboard)
                elif faculty == "юридический":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Юриспруденция', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Юриспруденция (очно-заочный)', keyboard=keyboard)
                elif faculty == "исторический":
                    send_message(vk_session, 'user_id', event.user_id, message= 'История', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Туризм', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Музеология и охрана объектов культурного наследия', keyboard=keyboard)
                elif faculty == "фспн":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Социальная', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Социальная работа', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Организация работы с молодежью', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Политология', keyboard=keyboard)
                elif faculty == "ивт":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Прикладная математика и информатика', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Фундаментальная информатика и информационные технологии', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Прикладная информатика', keyboard=keyboard)
                elif faculty == "математический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Математика и компьютерные науки", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Прикладная математика и информатика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информационная безопасность", keyboard=keyboard)
                elif faculty == "физический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Физика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Радиофизика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Радиотехника", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Инфокоммуникационные технологии и системы связи ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Электроника и наноэлектроника ", keyboard=keyboard)
                elif faculty == "биологии и экологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "Биология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Химия", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Экология и природопользование", keyboard=keyboard)
                elif faculty == "психологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "Основными направлениями научной работы на факультете являются:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Метакогнитивная психология деятельности", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология практического мышления и опыта", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология творческого профессионального мышления ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Социально-психологические закономерности функционирования коллективного субъекта профессиональной деятельности", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Методология, теория и практика профессиональной деятельности психолога-консультанта", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Интегративная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология вузовской адаптации", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Спортивная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Социальное познание в международных отношениях на примере коллективного субъекта (государства)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Организационная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Когнитивная психология и нейронаука", keyboard=keyboard)
                elif faculty == "филологии и коммуникации":
                    send_message(vk_session, 'user_id', event.user_id, message= "Филологическое обеспечение массовой коммуникации", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Филология и коммуникация: теоретический и прикладной аспект", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Филологическое обеспечение экспертной деятельности", keyboard=keyboard)
                elif faculty == "институт иностранных языков":
                    send_message(vk_session, 'user_id', event.user_id, message= "Иностранные языки и межкультурная коммуникация", keyboard=keyboard)

            elif response == "аспирантура":
                if faculty == "информация для абитуриентов":
                    send_message(vk_session, 'user_id', event.user_id, message= "Количество мест для приема по программам аспирантуры 2020", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация для поступающих на целевое обучение", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Проект расписания вступительных испытаний (для поступающих не по результатам ЕГЭ)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Список документов при подаче заявления 2020", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Правила приема в аспирантуру 2020/2021", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Сроки проведения приема", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Учет индивидуальных достижений", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Программы вступительных испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Перечень вступительных  испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Минимальное количество баллов и шкала оценивания", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Формы проведения вступительных испытаний", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Правила подачи и рассмотрения апелляций", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Особенности проведения вступительных испытаний для лиц с ограниченными возможностями здоровья", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация об особых правах и преимуществах", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Образцы договоров об оказании платных услуг", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Подача документов в электронной форме", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Места приема документов, почтовые и электронные адреса для направления документов", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информация об общежитии", keyboard=keyboard)
                elif faculty == "фспн":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Социальная структура, социальные институты и процессы', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Политические институты, процессы и технологии', keyboard=keyboard)
                elif faculty == "ивт":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Математика и механика', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Компьютерные и информационные науки', keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= 'Информатика и вычислительная техника', keyboard=keyboard)
                elif faculty == "математический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Математика и компьютерные науки", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Прикладная математика и информатика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Информационная безопасность", keyboard=keyboard)
                elif faculty == "физический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Физика и астрономия", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Электроника, радиотехника и системы связи ", keyboard=keyboard)
                elif faculty == "биологии и экологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "Микробиология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Физиология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Органическая химия", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Генетика", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Экология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Паразитология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Физиология и биохимия растений", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "Физическая химия", keyboard=keyboard)
                elif faculty == "психологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "Основными направлениями научной работы на факультете являются:", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Метакогнитивная психология деятельности", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология практического мышления и опыта", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология творческого профессионального мышления ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Социально-психологические закономерности функционирования коллективного субъекта профессиональной деятельности", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Методология, теория и практика профессиональной деятельности психолога-консультанта", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Интегративная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Психология вузовской адаптации", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Спортивная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Социальное познание в международных отношениях на примере коллективного субъекта (государства)", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Организационная психология", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "   Когнитивная психология и нейронаука", keyboard=keyboard)

            elif response == "среднее профессиональное образование":
                send_message(vk_session, 'user_id', event.user_id, message= "Контрольные цифры приема на 2020/2021 учебный год", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Перечень специальностей, по которым объявляется прием в 2020/2021 учебном году в соответствии с лицензией на осуществление образовательной деятельности", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Список документов при подаче заявления", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Программа творческого вступительного испытания по направлению 35.02.12 «Садово-парковое и ландшафтное строительство»", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Стоимость обучения в 2020-2021 учебном году Образцы договоров ", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "ПРАВИЛА ПРИЕМА В УНИВЕРСИТЕТСКИЙ КОЛЛЕДЖ  2020/2021", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Особенности проведения вступительных испытаний для инвалидов и лиц с ограниченными возможностями здоровья", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Подача документов в электронной форме", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Перечень и формы проведения вступительных испытаний", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Информация о необходимости прохождения поступающими обязательного предварительного медицинского осмотра", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Образцы договоров об оказании платных услуг", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message= "Форма проведения вступительных испытаний", keyboard=keyboard)

            elif response == "прикладная математика и информатика":
                send_message(vk_session, 'user_id', event.user_id, message= "прикладная математика и информатикад", keyboard=keyboard)
            elif response == "математика и компьютерные науки":
                send_message(vk_session, 'user_id', event.user_id, message= "математика и компьютерные науки", keyboard=keyboard)
            elif response == "информационная безопасность":
                send_message(vk_session, 'user_id', event.user_id, message= "информационная безопасность", keyboard=keyboard)
            elif response == "компьютерная безопасность":
                send_message(vk_session, 'user_id', event.user_id, message= "компьютерная безопасность", keyboard=keyboard)
            elif response == "прикладная математика и информатика":
                send_message(vk_session, 'user_id', event.user_id, message= "прикладная математика и информатика", keyboard=keyboard)
            elif response == "фундаментальная информатика и информационные технологии":
                send_message(vk_session, 'user_id', event.user_id, message= "фундаментальная информатика и информационные технологии", keyboard=keyboard)
            elif response == "прикладная информаиика в экономике":
                send_message(vk_session, 'user_id', event.user_id, message= "прикладная информаиика в экономике", keyboard=keyboard)
            elif response == "физика":
                send_message(vk_session, 'user_id', event.user_id, message= "физика", keyboard=keyboard)
            elif response == "радиофизика":
                send_message(vk_session, 'user_id', event.user_id, message= "радиофизика", keyboard=keyboard)
            elif response == "радиотехника":
                send_message(vk_session, 'user_id', event.user_id, message= "радиотехника", keyboard=keyboard)
            elif response == "инфокоммуникационные технологии и системы связи":
                send_message(vk_session, 'user_id', event.user_id, message= "инфокоммуникационные технологии и системы связи", keyboard=keyboard)
            elif response == "электроника и наноэлектроника":
                send_message(vk_session, 'user_id', event.user_id, message= "электроника и наноэлектроника", keyboard=keyboard)
            elif response == "химия":
                send_message(vk_session, 'user_id', event.user_id, message= "химия", keyboard=keyboard)
            elif response == "биология":
                send_message(vk_session, 'user_id', event.user_id, message= "биология", keyboard=keyboard)
            elif response == "экология и природопользование":
                send_message(vk_session, 'user_id', event.user_id, message= "экология и природопользование", keyboard=keyboard)
            elif response == "психология":
                send_message(vk_session, 'user_id', event.user_id, message= "психология", keyboard=keyboard)
            elif response == "экономика (бух. учёт, анализ и аудит)":
                send_message(vk_session, 'user_id', event.user_id, message= "экономика (бух. учёт, анализ и аудит)", keyboard=keyboard)
            elif response == "экономика (мировая экономика и международный бизнес)":
                send_message(vk_session, 'user_id', event.user_id, message= "экономика (мировая экономика и международный бизнес)", keyboard=keyboard)
            elif response == "экономика (финансы и кредит)":
                send_message(vk_session, 'user_id', event.user_id, message= "экономика (финансы и кредит)", keyboard=keyboard)
            elif response == "менеджмент":
                send_message(vk_session, 'user_id', event.user_id, message= "менеджмент", keyboard=keyboard)
            elif response == "государственное и муниципальное управление":
                send_message(vk_session, 'user_id', event.user_id, message= "государственное и муниципальное управление", keyboard=keyboard)
            elif response == "социология":
                send_message(vk_session, 'user_id', event.user_id, message= "социология", keyboard=keyboard)
            elif response == "социальная работа":
                send_message(vk_session, 'user_id', event.user_id, message= "социальная работа", keyboard=keyboard)
            elif response == "социальная работа (заочная)":
                send_message(vk_session, 'user_id', event.user_id, message= "социальная работа (заочная)", keyboard=keyboard)
            elif response == "организация работы с молодёжью":
                send_message(vk_session, 'user_id', event.user_id, message= "организация работы с молодёжью", keyboard=keyboard)
            elif response == "организация работы с молодёжью (заочная)":
                send_message(vk_session, 'user_id', event.user_id, message= "организация работы с молодёжью (заочная)", keyboard=keyboard)
            elif response == "политология":
                send_message(vk_session, 'user_id', event.user_id, message= "политология", keyboard=keyboard)
            elif response == "публичная политика и социальные науки":
                send_message(vk_session, 'user_id', event.user_id, message= "публичная политика и социальные науки", keyboard=keyboard)
            elif response == "юриспруденция":
                send_message(vk_session, 'user_id', event.user_id, message= "юриспруденция", keyboard=keyboard)
            elif response == "юриспруденция (очно-заочная)":
                send_message(vk_session, 'user_id', event.user_id, message= "юриспруденция (очно-заочная)", keyboard=keyboard)
            elif response == "прикладная филология":
                send_message(vk_session, 'user_id', event.user_id, message= "прикладная филология", keyboard=keyboard)
            elif response == "зарубежная филология":
                send_message(vk_session, 'user_id', event.user_id, message= "зарубежная филология", keyboard=keyboard)
            elif response == "реклама и связи с общественностью":
                send_message(vk_session, 'user_id', event.user_id, message= "реклама и связи с общественностью", keyboard=keyboard)
            elif response == "туризм":
                send_message(vk_session, 'user_id', event.user_id, message= "туризм", keyboard=keyboard)
            elif response == "история":
                send_message(vk_session, 'user_id', event.user_id, message= "история", keyboard=keyboard)

            elif response == "количество бюджетных мест":
                if faculty[-1] == "математический" and direction[-1] == "прикладная математика и информатика":
                    send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                elif direction[-1] == "математика и компьютерные науки":
                    send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                elif direction[-1] == "информационная безопасность":
                    send_message(vk_session, 'user_id', event.user_id, message= "20", keyboard=keyboard)
                elif direction[-1] == "компьютерная безопасность":
                    send_message(vk_session, 'user_id', event.user_id, message= "29", keyboard=keyboard)
                elif faculty[-1] == "ивт" and direction[-1] == "прикладная математика и информатика":
                    send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                elif direction[-1] == "фундаментальная информатика и информационные технологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "45", keyboard=keyboard)
                elif direction[-1] == "прикладная информаиика в экономике":
                    send_message(vk_session, 'user_id', event.user_id, message= "20", keyboard=keyboard)
                elif direction[-1] == "физика":
                    send_message(vk_session, 'user_id', event.user_id, message= "14", keyboard=keyboard)
                elif direction[-1] == "радиофизика":
                    send_message(vk_session, 'user_id', event.user_id, message= "20", keyboard=keyboard)
                elif direction[-1] == "радиотехника":
                    send_message(vk_session, 'user_id', event.user_id, message= "18", keyboard=keyboard)
                elif direction[-1] == "инфокоммуникационные технологии и системы связи":
                    send_message(vk_session, 'user_id', event.user_id, message= "30", keyboard=keyboard)
                elif direction[-1] == "электроника и наноэлектроника":
                    send_message(vk_session, 'user_id', event.user_id, message= "30", keyboard=keyboard)
                elif direction[-1] == "химия":
                    send_message(vk_session, 'user_id', event.user_id, message= "30", keyboard=keyboard)
                elif direction[-1] == "биология":
                    send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                elif direction[-1] == "экология и природопользование":
                    send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                elif direction[-1] == "психология":
                    send_message(vk_session, 'user_id', event.user_id, message= "24", keyboard=keyboard)
                elif direction[-1] == "экономика (бух. учёт, анализ и аудит)":
                    send_message(vk_session, 'user_id', event.user_id, message= "7", keyboard=keyboard)
                elif direction[-1] == "экономика (мировая экономика и международный бизнес)":
                    send_message(vk_session, 'user_id', event.user_id, message= "7", keyboard=keyboard)
                elif direction[-1] == "экономика (финансы и кредит)":
                    send_message(vk_session, 'user_id', event.user_id, message= "7", keyboard=keyboard)
                elif direction[-1] == "менеджмент":
                    send_message(vk_session, 'user_id', event.user_id, message= "7", keyboard=keyboard)
                elif direction[-1] == "государственное и муниципальное управление":
                    send_message(vk_session, 'user_id', event.user_id, message= "7", keyboard=keyboard)
                elif direction[-1] == "социология":
                    send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                elif direction[-1] == "социальная работа":
                    send_message(vk_session, 'user_id', event.user_id, message= "14", keyboard=keyboard)
                elif direction[-1] == "социальная работа (заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "9", keyboard=keyboard)
                elif direction[-1] == "организация работы с молодёжью":
                    send_message(vk_session, 'user_id', event.user_id, message= "14", keyboard=keyboard)
                elif direction[-1] == "организация работы с молодёжью (заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "9", keyboard=keyboard)
                elif direction[-1] == "политология":
                    send_message(vk_session, 'user_id', event.user_id, message= "10", keyboard=keyboard)
                elif direction[-1] == "публичная политика и социальные науки":
                    send_message(vk_session, 'user_id', event.user_id, message= "7", keyboard=keyboard)
                elif direction[-1] == "юриспруденция":
                    send_message(vk_session, 'user_id', event.user_id, message= "28", keyboard=keyboard)
                elif direction[-1] == "юриспруденция (очно-заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "29", keyboard=keyboard)
                elif direction[-1] == "прикладная филология":
                    send_message(vk_session, 'user_id', event.user_id, message= "8", keyboard=keyboard)
                elif direction[-1] == "зарубежная филология":
                    send_message(vk_session, 'user_id', event.user_id, message= "7", keyboard=keyboard)
                elif direction[-1] == "реклама и связи с общественностью":
                    send_message(vk_session, 'user_id', event.user_id, message= "-", keyboard=keyboard)
                elif direction[-1] == "туризм":
                    send_message(vk_session, 'user_id', event.user_id, message= "21", keyboard=keyboard)
                elif direction[-1] == "история":
                    send_message(vk_session, 'user_id', event.user_id, message= "27", keyboard=keyboard)

            elif response == "проходной балл":
                if faculty[-1] == "математический" and direction[-1] == "прикладная математика и информатика":
                    send_message(vk_session, 'user_id', event.user_id, message= "219", keyboard=keyboard)
                elif direction[-1] == "математика и компьютерные науки":
                    send_message(vk_session, 'user_id', event.user_id, message= "212", keyboard=keyboard)
                elif direction[-1] == "информационная безопасность":
                    send_message(vk_session, 'user_id', event.user_id, message= "226", keyboard=keyboard)
                elif direction[-1] == "компьютерная безопасность":
                    send_message(vk_session, 'user_id', event.user_id, message= "230", keyboard=keyboard)
                elif faculty[-1] == "ивт" and direction[-1] == "прикладная математика и информатика":
                    send_message(vk_session, 'user_id', event.user_id, message= "231", keyboard=keyboard)
                elif direction[-1] == "фундаментальная информатика и информационные технологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "233", keyboard=keyboard)
                elif direction[-1] == "прикладная информаиика в экономике":
                    send_message(vk_session, 'user_id', event.user_id, message= "230", keyboard=keyboard)
                elif direction[-1] == "физика":
                    send_message(vk_session, 'user_id', event.user_id, message= "179", keyboard=keyboard)
                elif direction[-1] == "радиофизика":
                    send_message(vk_session, 'user_id', event.user_id, message= "183", keyboard=keyboard)
                elif direction[-1] == "радиотехника":
                    send_message(vk_session, 'user_id', event.user_id, message= "181", keyboard=keyboard)
                elif direction[-1] == "инфокоммуникационные технологии и системы связи":
                    send_message(vk_session, 'user_id', event.user_id, message= "176", keyboard=keyboard)
                elif direction[-1] == "электроника и наноэлектроника":
                    send_message(vk_session, 'user_id', event.user_id, message= "187", keyboard=keyboard)
                elif direction[-1] == "химия":
                    send_message(vk_session, 'user_id', event.user_id, message= "202", keyboard=keyboard)
                elif direction[-1] == "биология":
                    send_message(vk_session, 'user_id', event.user_id, message= "198", keyboard=keyboard)
                elif direction[-1] == "экология и природопользование":
                    send_message(vk_session, 'user_id', event.user_id, message= "183", keyboard=keyboard)
                elif direction[-1] == "психология":
                    send_message(vk_session, 'user_id', event.user_id, message= "211", keyboard=keyboard)
                elif direction[-1] == "экономика (бух. учёт, анализ и аудит)":
                    send_message(vk_session, 'user_id', event.user_id, message= "240", keyboard=keyboard)
                elif direction[-1] == "экономика (мировая экономика и международный бизнес)":
                    send_message(vk_session, 'user_id', event.user_id, message= "240", keyboard=keyboard)
                elif direction[-1] == "экономика (финансы и кредит)":
                    send_message(vk_session, 'user_id', event.user_id, message= "240", keyboard=keyboard)
                elif direction[-1] == "менеджмент":
                    send_message(vk_session, 'user_id', event.user_id, message= "243", keyboard=keyboard)
                elif direction[-1] == "государственное и муниципальное управление":
                    send_message(vk_session, 'user_id', event.user_id, message= "240", keyboard=keyboard)
                elif direction[-1] == "социология":
                    send_message(vk_session, 'user_id', event.user_id, message= "227", keyboard=keyboard)
                elif direction[-1] == "социальная работа":
                    send_message(vk_session, 'user_id', event.user_id, message= "202", keyboard=keyboard)
                elif direction[-1] == "социальная работа (заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "177", keyboard=keyboard)
                elif direction[-1] == "организация работы с молодёжью":
                    send_message(vk_session, 'user_id', event.user_id, message= "202", keyboard=keyboard)
                elif direction[-1] == "организация работы с молодёжью (заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "184", keyboard=keyboard)
                elif direction[-1] == "политология":
                    send_message(vk_session, 'user_id', event.user_id, message= "210", keyboard=keyboard)
                elif direction[-1] == "публичная политика и социальные науки":
                    send_message(vk_session, 'user_id', event.user_id, message= "218", keyboard=keyboard)
                elif direction[-1] == "юриспруденция":
                    send_message(vk_session, 'user_id', event.user_id, message= "250", keyboard=keyboard)
                elif direction[-1] == "юриспруденция (очно-заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "203", keyboard=keyboard)
                elif direction[-1] == "прикладная филология":
                    send_message(vk_session, 'user_id', event.user_id, message= "232", keyboard=keyboard)
                elif direction[-1] == "зарубежная филология":
                    send_message(vk_session, 'user_id', event.user_id, message= "261", keyboard=keyboard)
                elif direction[-1] == "реклама и связи с общественностью":
                    send_message(vk_session, 'user_id', event.user_id, message= "-", keyboard=keyboard)
                elif direction[-1] == "туризм":
                    send_message(vk_session, 'user_id', event.user_id, message= "222", keyboard=keyboard)
                elif direction[-1] == "история":
                    send_message(vk_session, 'user_id', event.user_id, message= "225", keyboard=keyboard)

            elif response == "стоимость обучения":
                if faculty[-1] == "математический" and direction[-1] == "прикладная математика и информатика":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "математика и компьютерные науки":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "информационная безопасность":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "компьютерная безопасность":
                    send_message(vk_session, 'user_id', event.user_id, message= "-", keyboard=keyboard)
                elif faculty[-1] == "ивт" and direction[-1] == "прикладная математика и информатика":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "фундаментальная информатика и информационные технологии":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "прикладная информаиика в экономике":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "физика":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "радиофизика":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "радиотехника":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "инфокоммуникационные технологии и системы связи":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802 (оч.) / 62181 (заоч.)", keyboard=keyboard)
                elif direction[-1] == "электроника и наноэлектроника":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "химия":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "биология":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "экология и природопользование":
                    send_message(vk_session, 'user_id', event.user_id, message= "132802", keyboard=keyboard)
                elif direction[-1] == "психология":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "экономика (бух. учёт, анализ и аудит)":
                    send_message(vk_session, 'user_id', event.user_id, message= "128097 (оч.) / 58097 (заоч.)", keyboard=keyboard)
                elif direction[-1] == "экономика (мировая экономика и международный бизнес)":
                    send_message(vk_session, 'user_id', event.user_id, message= "128097", keyboard=keyboard)
                elif direction[-1] == "экономика (финансы и кредит)":
                    send_message(vk_session, 'user_id', event.user_id, message= "128097", keyboard=keyboard)
                elif direction[-1] == "менеджмент":
                    send_message(vk_session, 'user_id', event.user_id, message= "128097 (оч.) / 58097 (заоч.)", keyboard=keyboard)
                elif direction[-1] == "государственное и муниципальное управление":
                    send_message(vk_session, 'user_id', event.user_id, message= "128097 (оч.) / 58097 (заоч.)", keyboard=keyboard)
                elif direction[-1] == "социология":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "социальная работа":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "социальная работа (заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "49749", keyboard=keyboard)
                elif direction[-1] == "организация работы с молодёжью":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "организация работы с молодёжью (заочная)":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "политология":
                    send_message(vk_session, 'user_id', event.user_id, message= "120628", keyboard=keyboard)
                elif direction[-1] == "публичная политика и социальные науки":
                    send_message(vk_session, 'user_id', event.user_id, message= "73327", keyboard=keyboard)
                elif direction[-1] == "юриспруденция":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "юриспруденция (очно-заочная)":
                    send_message(vk_session, 'user_id', event.user_id   , message= "114738", keyboard=keyboard)
                elif direction[-1] == "прикладная филология":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "зарубежная филология":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738 (оч.) / 55164 (заоч.)", keyboard=keyboard)
                elif direction[-1] == "реклама и связи с общественностью":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "туризм":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)
                elif direction[-1] == "история":
                    send_message(vk_session, 'user_id', event.user_id, message= "114738", keyboard=keyboard)

            elif response == "способы подачи документов":
                send_message(vk_session, 'user_id', event.user_id, message= "Способы подачи документов", keyboard=keyboard)

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

            elif response == "узнать свой рейтинг":
                send_message(vk_session, 'user_id', event.user_id, message= full_info('Дык Фам'))

            elif response == "специальности":
                send_message(vk_session, 'user_id', event.user_id, message= 'Специальности:', keyboard=keyboard)

            elif response == "общая информация":
                send_message(vk_session, 'user_id', event.user_id, message= 'Общая информация:', keyboard=keyboard)

            elif response == "информация по факультетам":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите факультет:', keyboard=keyboard)

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
                send_message(vk_session, 'user_id', event.user_id, message= 'Как поступить:', keyboard=keyboard)

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
