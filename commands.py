from vk_api.keyboard import VkKeyboardColor


def start_button(keyboard, keyboard_history):
    keyboard.add_button('Общая информация', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Информация по факультетам', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Узнать свой рейтинг', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Задать вопрос', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def back(keyboard, keyboard_history):
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def return_keyboard(keyboard_history):
    keyboard_history = keyboard_history[:-1]
    return keyboard_history[-1]


def subscribe(keyboard, keyboard_history):
    keyboard.add_button('Информация о вузе', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Контакты', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Подписаться на новости', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def unsubscribe(keyboard, keyboard_history):
    keyboard.add_button('Информация о вузе', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Контакты', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Отписаться от новостей', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def info(keyboard, keyboard_history):
    keyboard.add_button('История вуза', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Учёный совет', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Основные документы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def contacts(keyboard, keyboard_history):
    keyboard.add_button('Контакты вуза', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Контакты приёмной комиссии', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Контакты приёмной комиссии (для иностр.)', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def f_cks(keyboard, keyboard_history):
    keyboard.add_button('Юридический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Экономический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ИВТ', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Математический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Физический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Биологии и экологии', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Психологический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Филологии и коммуникации', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Институт ин. языков', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('ФСПН', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Исторический', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Университетский колледж', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def f_ck(keyboard, keyboard_history):
    keyboard.add_button('Как поступить?', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Где трудиться?', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Информация о факультете', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Контакты факультета', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Подписаться на рассылку факультета', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def levels(keyboard, keyboard_history):
    keyboard.add_button('Бакалавриат и специалитет', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Магистратура', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Аспирантура', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def math_bachelor(keyboard, keyboard_history):
    keyboard.add_button('Математика и компьютерные науки', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Прикладная математика и информатика', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Информационная безопасность", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Компьютерная безопасность", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def math_graduate(keyboard, keyboard_history):
    keyboard.add_button("Математика и механика", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Информатика и вычислительная техника", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Информационная безопасность", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def it_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Прикладная математика и информатика", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Фундаментальная информатика", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Прикладная математика и информатика", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def it_graduate(keyboard, keyboard_history):
    keyboard.add_button("Математика и механика", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Информатика и вычислительная техника", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Компьютерные и информационные науки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def physical_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Физика", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Радиофизика", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Радиотехника", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Инфокоммуникационные технологии и системы связи", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Электроника и наноэлектроника", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def physical_graduate(keyboard, keyboard_history):
    keyboard.add_button("Физика и астрономия", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Электроника, радиоэлектроника и системы связи", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def economic_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Экономика", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Менеджмент", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Государственное и муниципальное управление", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def economic_graduate(keyboard, keyboard_history):
    keyboard.add_button("Экономика", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Экономика", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Экономика", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Экономика", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def law_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Юриспруденция", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Юриспруденция (очно-заочный)", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def law_graduate(keyboard, keyboard_history):
    keyboard.add_button("Юриспруденция", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Юриспруденция", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Юриспруденция", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Юриспруденция", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def social_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Социология", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Социальная работа", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Политология", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Публичная политика и социальные науки", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Организация работы с молодёжью", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def social_graduate(keyboard, keyboard_history):
    keyboard.add_button("Социологические науки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Политические науки и регионоведение", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Политические науки и регионоведение", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def historical_bachelor(keyboard, keyboard_history):
    keyboard.add_button("История", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Туризм", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Реклама и связи с общественностью", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def historical_graduate(keyboard, keyboard_history):
    keyboard.add_button("Исторические науки и археология", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Исторические науки и археология", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def biology_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Биология", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Химия", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Экология и природопользование", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def biology_graduate(keyboard, keyboard_history):
    keyboard.add_button("Химические науки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Биологические науки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def psycological_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Психология", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def psycological_graduate(keyboard, keyboard_history):
    keyboard.add_button("Психологические науки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Психологические науки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def feel_f_ck_bachelor(keyboard, keyboard_history):
    keyboard.add_button("Прикладная филология (русский язык)", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def feel_f_ck_graduate(keyboard, keyboard_history):
    keyboard.add_button("Образование и педагогические науки", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Языкознание и литературоведение", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Языкознание и литературоведение", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def variants(keyboard, keyboard_history):
    keyboard.add_button('Лично', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('В электронной форме', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('По почте', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def direction_menu(keyboard, keyboard_history):
    keyboard.add_button('Количество бюджетных мест', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Проходной балл', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Стоимость обучения', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def rating(keyboard, keyboard_history):
    keyboard.add_button('Изменить', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)
    keyboard_history.append(keyboard)
    return keyboard


def save(keyboard, keyboard_history):
    keyboard.add_button('Да', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Нет', color=VkKeyboardColor.NEGATIVE)
    keyboard_history.append(keyboard)
    return keyboard


def change(keyboard, keyboard_history):
    keyboard.add_button('Изменить', color=VkKeyboardColor.PRIMARY)
    keyboard_history.append(keyboard)
    return keyboard