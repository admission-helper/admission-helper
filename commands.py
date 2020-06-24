from vk_api.keyboard import VkKeyboardColor

def add_button(keyboard, msg, color):
    if color == 'positive':
        keyboard.add_button(msg, color=VkKeyboardColor.POSITIVE)
    elif color == 'negative':
        keyboard.add_button(msg, color=VkKeyboardColor.NEGATIVE)
    elif color == 'primary':
        keyboard.add_button(msg, color=VkKeyboardColor.PRIMARY)
    elif color == 'default':
        keyboard.add_button(msg, color=VkKeyboardColor.DEFAULT)
    return keyboard

def add_line_button(keyboard, msg, color):
    keyboard = add_button(keyboard, msg, color)
    keyboard.add_line()
    return keyboard

def start_button(keyboard):
    keyboard = add_line_button(keyboard, 'Приёмная комиссия', 'positive')
    keyboard = add_line_button(keyboard, 'Узнать свой рейтинг', 'positive')
    keyboard = add_line_button(keyboard, 'Общая информация', 'primary')
    keyboard = add_button(keyboard, 'Информация по факультетам', 'primary')
    return keyboard

def level(keyboard):
    keyboard = add_line_button(keyboard, 'Бакалавриат и специалитет', 'primary')
    keyboard = add_line_button(keyboard, 'Магистратура', 'primary')
    keyboard = add_line_button(keyboard, 'Аспирантура', 'primary')
    keyboard = add_line_button(keyboard, 'Среднее профессиональное образование', 'primary')
    keyboard = add_button(keyboard, 'Информация по факультетам', 'default')
    return keyboard

def study_level(keyboard):
    keyboard.add_button('Бакалавриат и специалитет', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Магистратура', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Аспирантура', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def open(keyboard):
    keyboard.add_button('Напомнить о проведении', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Смотреть видео о факультете', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Виртуальный курс по корпусам университета', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()

def back(keyboard):
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def sc(keyboard):
    keyboard.add_button('Информация для абитуриентов', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Информация по факультетам', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Контакты приёмной комиссии', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('График работы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Дни открытых дверей', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def sc_contacts(keyboard):
    keyboard.add_button('Адрес', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Телефон', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Email', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Skype', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Телефон (для иностранных граждан)', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Email (для иностранных граждан)', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

# узнать свой рейтинг

def info(keyboard):
    keyboard.add_button('Информация о вузе', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Дни открытых дверей', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Подписаться на новости', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

def info_university(keyboard):
    keyboard.add_button('История', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Контакты приёмной комиссии', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('График работы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

def faculties(keyboard):
    keyboard.add_button('Юридический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Экономический', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('ИВТ', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Математический', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Физический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Биологии и экологии', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Психологический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Филологии и коммуникации', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Институт ин. языков', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('ФСПН', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Исторический', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Университетский колледж', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def f_ck(keyboard):
    keyboard.add_button('Как поступить?', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Где трудиться?', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('О факультете', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Узнать свой рейтинг', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Контакты факультета', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Подписаться на рассылку', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def economic_directions(keyboard):
    keyboard.add_button("Экономика", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Менеджмент", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Государственное и муниципальное управление", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def law_directions(keyboard):
    keyboard.add_button("Юриспруденция", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Юриспруденция (очно-заочный)", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def historical_directions(keyboard):
    keyboard.add_button("Социология", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Социальная работа", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Политология", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Публичная политика и социальные науки", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Организация работы с молодёжью", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def social_directions(keyboard):
    keyboard.add_button("История", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Туризм", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Реклама и связи с общественностью", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def it_directions(keyboard):
    keyboard.add_button("Прикладная математика и информатика", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Фундаментальная информатика и информационные технологии", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Прикладная математика и информатика", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def math_directions(keyboard):
    keyboard.add_button('Математика и компьютерные науки', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Прикладная математика и информатика', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Информационная безопасность", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Компьютерная безопасность", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def physical_directions(keyboard):
    keyboard.add_button("Физика", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Радиофизика", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("Радиотехника", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Инфокоммуникационные технологии и системы связи ", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Электроника и наноэлектроника", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def biology_directions(keyboard):
    keyboard.add_button("Биология", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Химия", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Экология и природопользование", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def psycology_directions(keyboard):
    keyboard.add_button("Психология", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def feel_f_ck_directions(keyboard):
    keyboard.add_button("Прикладная филология (русский язык)", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    return keyboard

def how(keyboard):
    keyboard.add_button('Выберите направление', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Способы подачи', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Задайте вопрос', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def direction_menu(keyboard):
    keyboard.add_button('Количество бюджетных мест', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Проходной балл', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Стоимость обучения', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def f_ck_info(keyboard):
    keyboard.add_button('Направления', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Кафедры", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("История", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Руководство", color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

def sc_math_f_ck_directions(keyboard):
    keyboard.add_button('Математика и компьютерные науки', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Прикладная математика и информатика', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Информационная безопасность', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Компьютерная безопасность', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def sc_math_f_ck_directions_direction(keyboard):
    keyboard.add_button('Срок обучения', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Основа обучения', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Изучаемые дисциплины', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Кем вы сможете работать', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def sc_math_f_ck_questions(keyboard):
    keyboard.add_button('Сколько я буду учиться?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Какую квалификацию мне присвоят?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Какие экзамены мне нужно сдавать?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()

def sc_math_f_ck_questions_training(keyboard):
    keyboard.add_button('Математика и компьютерные науки', color=VkKeyboardColor.PRIMARY) # 4 года
    keyboard.add_line()
    keyboard.add_button('Прикладная математика и информатика', color=VkKeyboardColor.PRIMARY) # 4 года
    keyboard.add_line()
    keyboard.add_button('Информационная безопасность', color=VkKeyboardColor.PRIMARY) # 4 года
    keyboard.add_line()
    keyboard.add_button('Компьютерная безопасность', color=VkKeyboardColor.PRIMARY) # 4 года
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT) # 5,5 лет
    return keyboard

def sc_math_f_ck_questions(keyboard):
    keyboard.add_button('Как поступить?', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Как учиться?', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Где трудиться?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def submit_documents(keyboard):
    keyboard.add_button('Посмотреть направления', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Посмотреть проходные баллы', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Информация о вузе', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Новости', color=VkKeyboardColor.DEFAULT)
    return keyboard