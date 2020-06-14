from vk_api.keyboard import VkKeyboardColor

def start_button(keyboard):
    keyboard.add_button('Приёмная комиссия', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Узнать свой рейтинг', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Общая информация', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Информация по факультетам', color=VkKeyboardColor.PRIMARY)
    return keyboard

def sc(keyboard):
    keyboard.add_button('Информация для абитуриентов', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Контакты приёмной комиссии', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def sc_info(keyboard):
    keyboard.add_button('Список документов при подаче заявления 2020', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Согласие на обработку персональных данных', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Памятка для абитуриента', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Стоимость обучения в 2020-2021 учебном году', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Положение о скидках по оплате обучения 2019', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Правила приёма по программам бакалавриата и специалитета', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Памятка для абитуриента', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def sc_contacts(keyboard):
    keyboard.add_button('Адрес', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Телефон', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Email', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Skype', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Телефон (для иностранных граждан)', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Email (для иностранных граждан)', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

def questions(keyboard):
    keyboard.add_button('Адрес', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()

# узнать свой рейтинг

def info(keyboard):
    keyboard.add_button('День открытых дверей', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Школьникам', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Контакты', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

def faculties(keyboard):
    keyboard.add_button('Юридический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Экономический', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Математический', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Физический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Психологии', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Биологический', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Исторический', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Филологический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Институт ин. языков', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('ФСПН', color=VkKeyboardColor.POSITIVE)
    return keyboard

def sc_math_f_ck(keyboard):
    keyboard.add_button('Направления', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Способы подачи документов', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Узнать свой рейтинг', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Контакты', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard

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

def back(keyboard):
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    return keyboard