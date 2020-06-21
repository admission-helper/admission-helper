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
from chat_bot import chat

#login, password='login','password'
# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()
token ='d42dbd70cec94a365ea175cdf198e47cf64e3ff0f61510640f2e2c32837c383294464ca6a36eda1a60c98'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

text_history = ["Вы и так в самом низу"]
faculty = ["Да"]
direction = ["Да"]

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'старт':
        keyboard = start_button(keyboard)

    elif response == "назад":
        keyboard = keyboard_history[-1]

    elif response == "приёмная комиссия":
        text_history.append("старт")
        keyboard = sc(keyboard)

    elif response == "информация для абитуриентов":
        faculty.append("информация для абитуриентов")
        keyboard = level(keyboard)

    elif response == "бакалавриат и специалитет":
        keyboard = back(keyboard)

    elif response == "магистратура":
        keyboard = back(keyboard)

    elif response == "аспирантура":
        keyboard = back(keyboard)

    elif response == "среднее профессиональное образование":
        keyboard = back(keyboard)

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

    elif response == 'контакты приёмной комиссии':
        keyboard = sc_contacts(keyboard)

    elif response == 'информация по факультетам':
        text_history.append("старт")
        keyboard = faculties(keyboard)

    elif response == "юридический":
        faculty.append("юридический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "экономический":
        faculty.append("экономический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "информатики и вычислительной техники":
        faculty.append("информатики и вычислительной техники")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "математический":
        faculty.append("математический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "физический":
        faculty.append("физический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "биологическии и экологии":
        faculty.append("биологическии и экологии")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "психологический":
        faculty.append("психологический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "филологический":
        faculty.append("филологический")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "институт иностранных языков":
        faculty.append("институт иностранных языков")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "факультет социально политических наук":
        faculty.append("факультет социально политический наук")
        text_history.append("информация по факультетам")
        keyboard = f_ck(keyboard)

    elif response == "количество бюджетных мест":
        keyboard = back(keyboard)

    elif response == "проходной балл":
        keyboard = back(keyboard)

    elif response == "стоимость обучения":
        keyboard = back(keyboard)

    elif response == "как поступить?":
        keyboard = how(keyboard)

    elif response == "выберите направление":
        if faculty[-1] == "экономический":
            keyboard = economic_directions(keyboard)
        elif faculty[-1] == "юридический":
            keyboard = law_directions(keyboard)
        elif faculty[-1] == "исторический":
            keyboard = history_directions(keyboard)
        elif faculty[-1] == "факультет социально политических наук":
            keyboard = social_directions(keyboard)
        elif faculty[-1] == "информатики и вычислительной техники":
            keyboard = it_directions(keyboard)
        elif faculty[-1] == "математический":
            keyboard = math_directions(keyboard)
        elif faculty[-1] == "физический":
            keyboard = physical_directions(keyboard)
        elif faculty[-1] == "биологии и экологии":
            keyboard = biology_directions(keyboard)
        elif faculty[-1] == "психологии":
            keyboard = psycology_directions(keyboard)
        elif faculty[-1] == "филологии и коммуникации":
            keyboard = feel_f_ck_directions(keyboard)
        else:
            keyboard = back(keyboard)

    elif response == "прикладная математика и информатика":
        direction.append("прикладная математика и информатика")
        keyboard = direction_menu(keyboard)
    elif response == "математика и компьютерные науки":
        direction.append("математика и компьютерные науки")
        keyboard = direction_menu(keyboard)
    elif response == "информационная безопасность":
        direction.append("информационная безопасность")
        keyboard = direction_menu(keyboard)
    elif response == "компьютерная безопасность":
        direction.append("компьютерная безопасность")
        keyboard = direction_menu(keyboard)
    elif response == "прикладная математика и информатика":
        direction.append("прикладная математика и информатика")
        keyboard = direction_menu(keyboard)
    elif response == "фундаментальная информатика и информационные технологии":
        direction.append("фундаментальная информатика и информационные технологии")
        keyboard = direction_menu(keyboard)
    elif response == "прикладная информаиика в экономике":
        direction.append("прикладная информаиика в экономике")
        keyboard = direction_menu(keyboard)
    elif response == "физика":
        direction.append("физика")
        keyboard = direction_menu(keyboard)
    elif response == "радиофизика":
        direction.append("радиофизика")
        keyboard = direction_menu(keyboard)
    elif response == "радиотехника":
        direction.append("радиотехника")
        keyboard = direction_menu(keyboard)
    elif response == "инфокоммуникационные технологии и системы связи":
        direction.append("инфокоммуникационные технологии и системы связи")
        keyboard = direction_menu(keyboard)
    elif response == "электроника и наноэлектроника":
        direction.append("электроника и наноэлектроника")
        keyboard = direction_menu(keyboard)
    elif response == "химия":
        direction.append("химия")
        keyboard = direction_menu(keyboard)
    elif response == "биология":
        direction.append("биология")
        keyboard = direction_menu(keyboard)
    elif response == "экология и природопользование":
        direction.append("экология и природопользование")
        keyboard = direction_menu(keyboard)
    elif response == "психология":
        direction.append("психология")
        keyboard = direction_menu(keyboard)
    elif response == "экономика (бух. учёт, анализ и аудит)":
        direction.append("экономика (бух. учёт, анализ и аудит)")
        keyboard = direction_menu(keyboard)
    elif response == "экономика (мировая экономика и международный бизнес)":
        direction.append("экономика (мировая экономика и международный бизнес)")
        keyboard = direction_menu(keyboard)
    elif response == "экономика (финансы и кредит)":
        direction.append("экономика (финансы и кредит)")
        keyboard = direction_menu(keyboard)
    elif response == "менеджмент":
        direction.append("менеджмент")
        keyboard = direction_menu(keyboard)
    elif response == "государственное и муниципальное управление":
        direction.append("государственное и муниципальное управление")
        keyboard = direction_menu(keyboard)
    elif response == "социология":
        direction.append("социология")
        keyboard = direction_menu(keyboard)
    elif response == "социальная работа":
        direction.append("социальная работа")
        keyboard = direction_menu(keyboard)
    elif response == "социальная работа (заочная)":
        direction.append("социальная работа (заочная)")
        keyboard = direction_menu(keyboard)
    elif response == "организация работы с молодёжью":
        direction.append("организация работы с молодёжью")
        keyboard = direction_menu(keyboard)
    elif response == "организация работы с молодёжью (заочная)":
        direction.append("организация работы с молодёжью (заочная)")
        keyboard = direction_menu(keyboard)
    elif response == "политология":
        direction.append("политология")
        keyboard = direction_menu(keyboard)
    elif response == "публичная политика и социальные науки":
        direction.append("публичная политика и социальные науки")
        keyboard = direction_menu(keyboard)
    elif response == "юриспруденция":
        direction.append("юриспруденция")
        keyboard = direction_menu(keyboard)
    elif response == "юриспруденция (очно-заочная)":
        direction.append("юриспруденция (очно-заочная)")
        keyboard = direction_menu(keyboard)
    elif response == "прикладная филология":
        direction.append("прикладная филология")
        keyboard = direction_menu(keyboard)
    elif response == "зарубежная филология":
        direction.append("зарубежная филология")
        keyboard = direction_menu(keyboard)
    elif response == "реклама и связи с общественностью":
        direction.append("реклама и связи с общественностью")
        keyboard = direction_menu(keyboard)
    elif response == "туризм":
        direction.append("туризм")
        keyboard = direction_menu(keyboard)
    elif response == "история":
        direction.append("история")
        keyboard = direction_menu(keyboard)

    elif response == "направления":
        keyboard = level(keyboard)

    elif response == "где трудиться?":
        keyboard = back(keyboard)

    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        return keyboard.get_empty_keyboard()

    print(faculty)

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

        send(response)

        if event.from_user and not event.from_me:
            # if response == "котики":
            #     attachment = get_pictures.get(vk_session, -130670107, session_api)
            #     send_message(vk_session, 'user_id', event.user_id, message='Держи котиков!', attachment=attachment, keyboard=keyboard)
            if response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)

            elif response == "старт":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды:', keyboard=keyboard)

            elif response == "чат":
                send_message(vk_session, 'user_id', event.user_id, message= 'Задайте вопрос боту: ', keyboard=keyboard)

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
                elif faculty == "ИВТ":
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
                    send_message(vk_session, 'user_id', event.user_id, message= "Психология", keyboard=keyboard)
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
                elif faculty == "ИВТ":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Математика и механика\nКомпьютерные и информационные науки\nИнформатика и вычислительная техника', keyboard=keyboard)
                elif faculty == "математический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Математика и компьютерные науки\nПрикладная математика и информатика\n", keyboard=keyboard)
                elif faculty == "физический":
                    send_message(vk_session, 'user_id', event.user_id, message= "Физика и астрономия\nЭлектроника, радиотехника и системы связи ", keyboard=keyboard)
                    send_message(vk_session, 'user_id', event.user_id, message= "", keyboard=keyboard)
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
                send_message(vk_session, 'user_id', event.user_id, message= "прикладная математика и информатика", keyboard=keyboard)
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
                if faculty[-1] == "математический":
                    if direction[-1] == "прикладная математика и информатика":
                        send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                    elif direction[-1] == "математика и компьютерные науки":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "информационная безопасность":
                        send_message(vk_session, 'user_id', event.user_id, message= "20", keyboard=keyboard)
                    elif direction[-1] == "компьютерная безопасность":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "информатики и вычислительной техники":
                    if direction[-1] == "прикладная математика и информатика":
                        send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                    elif direction[-1] == "фундаментальная информатика и информационные технологии":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "прикладная информаиика в экономике":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "физический":
                    if direction[-1] == "физика":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "радиофизика":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "радиотехника":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "инфокоммуникационные технологии и системы связи":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "электроника и наноэлектроника":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "биологический":
                    if direction[-1] == "химия":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "биология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экология и природопользование":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "психологический":
                    if direction[-1] == "психология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "экономический":
                    if direction[-1] == "экономика (бух. учёт, анализ и аудит)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экономика (мировая экономика и международный бизнес)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экономика (финансы и кредит)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "менеджмент":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "государственное и муниципальное управление":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "фспн":
                    if direction[-1] == "социология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "социальная работа":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "социальная работа (заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "организация работы с молодёжью":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "организация работы с молодёжью (заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "политология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "публичная политика и социальные науки":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "юридический":
                    if direction[-1] == "юриспруденция":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "юриспруденция (очно-заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "прикладная филология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "зарубежная филология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "исторический":
                    if direction[-1] == "реклама и связи с общественностью":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "туризм":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "история":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

            elif response == "проходной балл":
                if faculty[-1] == "математический":
                    if direction[-1] == "прикладная математика и информатика":
                        send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                    elif direction[-1] == "математика и компьютерные науки":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "информационная безопасность":
                        send_message(vk_session, 'user_id', event.user_id, message= "20", keyboard=keyboard)
                    elif direction[-1] == "компьютерная безопасность":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "информатики и вычислительной техники":
                    if direction[-1] == "прикладная математика и информатика":
                        send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                    elif direction[-1] == "фундаментальная информатика и информационные технологии":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "прикладная информаиика в экономике":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "физический":
                    if direction[-1] == "физика":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "радиофизика":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "радиотехника":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "инфокоммуникационные технологии и системы связи":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "электроника и наноэлектроника":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "биологический":
                    if direction[-1] == "химия":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "биология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экология и природопользование":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "психологический":
                    if direction[-1] == "психология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "экономический":
                    if direction[-1] == "экономика (бух. учёт, анализ и аудит)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экономика (мировая экономика и международный бизнес)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экономика (финансы и кредит)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "менеджмент":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "государственное и муниципальное управление":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "фспн":
                    if direction[-1] == "социология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "социальная работа":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "социальная работа (заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "организация работы с молодёжью":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "организация работы с молодёжью (заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "политология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "публичная политика и социальные науки":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "юридический":
                    if direction[-1] == "юриспруденция":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "юриспруденция (очно-заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "прикладная филология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "зарубежная филология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "исторический":
                    if direction[-1] == "реклама и связи с общественностью":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "туризм":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "история":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

            elif response == "стоимость обучения":
                if faculty[-1] == "математический":
                    if direction[-1] == "прикладная математика и информатика":
                        send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                    elif direction[-1] == "математика и компьютерные науки":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "информационная безопасность":
                        send_message(vk_session, 'user_id', event.user_id, message= "20", keyboard=keyboard)
                    elif direction[-1] == "компьютерная безопасность":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "информатики и вычислительной техники":
                    if direction[-1] == "прикладная математика и информатика":
                        send_message(vk_session, 'user_id', event.user_id, message= "50", keyboard=keyboard)
                    elif direction[-1] == "фундаментальная информатика и информационные технологии":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "прикладная информаиика в экономике":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "физический":
                    if direction[-1] == "физика":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "радиофизика":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "радиотехника":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "инфокоммуникационные технологии и системы связи":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "электроника и наноэлектроника":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "биологический":
                    if direction[-1] == "химия":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "биология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экология и природопользование":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "психологический":
                    if direction[-1] == "психология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "экономический":
                    if direction[-1] == "экономика (бух. учёт, анализ и аудит)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экономика (мировая экономика и международный бизнес)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "экономика (финансы и кредит)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "менеджмент":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "государственное и муниципальное управление":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "фспн":
                    if direction[-1] == "социология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "социальная работа":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "социальная работа (заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "организация работы с молодёжью":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "организация работы с молодёжью (заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "политология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "публичная политика и социальные науки":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "юридический":
                    if direction[-1] == "юриспруденция":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "юриспруденция (очно-заочная)":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "прикладная филология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "зарубежная филология":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

                elif faculty[-1] == "исторический":
                    if direction[-1] == "реклама и связи с общественностью":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "туризм":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)
                    elif direction[-1] == "история":
                        send_message(vk_session, 'user_id', event.user_id, message= "15", keyboard=keyboard)

            elif response == "назад":
                send_message(vk_session, 'user_id', event.user_id, message= text_history[-1], keyboard=keyboard)

            elif response == "вопрос":
                send_message(vk_session, 'user_id', event.user_id, message= "Задайте мне вопрос. Я отвечу в течение дня.", keyboard=keyboard)

            elif response == "приёмная комиссия":
                send_message(vk_session, 'user_id', event.user_id, message= 'Приёмная комиссия:', keyboard=keyboard)

            elif response == "информация для абитуриентов":
                send_message(vk_session, 'user_id', event.user_id, message= 'Информация для абитуриентов:', keyboard=keyboard)

            elif response == "контакты приёмной комиссии":
                send_message(vk_session, 'user_id', event.user_id, message= 'Контакты приёмной комиссии:', keyboard=keyboard)

            elif response == "адрес":
                send_message(vk_session, 'user_id', event.user_id, message="150000, г. Ярославль, ул.Кирова 8/10, каб. 102", keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message='Как до нас добраться:', keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message='Проезд от вокзала «Ярославль-Главный» троллейбусом №1 до остановки «пл. Волкова» или Любым видом общественного транспорта до остановки «пл. Богоявления»', keyboard=keyboard)

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
                send_message(vk_session, 'user_id', event.user_id, message= full_info('Студент 1'))

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

            elif response == "ИВТ":
                send_message(vk_session, 'user_id', event.user_id, message= 'ИВТ:', keyboard=keyboard)

            elif response == "математический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Математический:', keyboard=keyboard)

            elif response == "физический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Физический:', keyboard=keyboard)

            elif response == "биологический":
                send_message(vk_session, 'user_id', event.user_id, message= 'Биологический:', keyboard=keyboard)

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
                send_message(vk_session, 'user_id', event.user_id, message= 'Факультет социально политических наук:', keyboard=keyboard)

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
                send_message(vk_session, 'user_id', event.user_id, message= full_info('Студент 1'))

            else:
                send_message(vk_session, 'user_id', event.user_id, message= '')


        # elif event.from_chat :
        #     if response == "котики":
        #         attachment = get_pictures.get(vk_session, -130670107, session_api)
        #         print(attachment)
        #         send_message(vk_session, 'chat_id', event.chat_id, message='Держите котиков!', attachment= attachment)
        #print('-' * 30)l