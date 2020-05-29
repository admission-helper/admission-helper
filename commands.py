from vk_api.keyboard import VkKeyboardColor

def start_button(keyboard):
    keyboard.add_button('Общая информация', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Информация по факультетам', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Рейтинг', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Не знаю куда пойти', color=VkKeyboardColor.PRIMARY)
    return keyboard

def info_button(keyboard):
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