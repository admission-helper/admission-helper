from os import pread
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text
from vkbottle.tools.dev_tools import keyboard
from vkbottle.tools.dev_tools.keyboard.action import Payload
from vkbottle.tools.dev_tools.mini_types.bot.message import message_min
from config import TOKEN
import uvloop

bot = Bot(TOKEN)



KEYBOARD = (
    Keyboard(one_time=True)
    .add(Text("Калькулятор ЕГЭ"))
    .add(Text("О боте"))
    .get_json()
)

subject = ''

@bot.on.message(payload={"subject": "subject"})
async def score_handler(message: Message) -> None:

    global subject
    subject = message.text

    keyboard = Keyboard(one_time=True, inline=False)

    await message.answer('Введите баллы')

@bot.on.message(text=['Калькулятор ЕГЭ'])
async def subject_handler(message: Message) -> None:

    SUBJECTS = ("Математика", "Информатика", "История", 
                "Обществознание", "Физика", "Химия", 
                "Биология", "Литература")

    keyboard = Keyboard(one_time=True, inline=False)

    for i, subject in enumerate(SUBJECTS):
        keyboard.add(Text(subject, {"subject": "subject"}))
        if i % 2 != 0:
            keyboard.row()

    keyboard.add(Text("Назад", {"subject": "back"}))
    keyboard.add(Text("Далее", {"subject": "next"}))

    ANSWER_TEXT = 'Выберите экзамен, если все экзамены введены, нажмите "Далее"'

    await message.answer(ANSWER_TEXT, keyboard=keyboard.get_json())

@bot.on.message(payload={"subject": "back"})
@bot.on.message(text=['Начать'])
async def back_subject_handler(message: Message) -> None:

    KEYBOARD = (
        Keyboard(one_time=True)
        .add(Text("Калькулятор ЕГЭ"))
        .add(Text("О боте"))
        .get_json()
    )

    await message.answer('Я вас категорически приветствую', keyboard=KEYBOARD)

@bot.on.message(payload={"subject": "next"})
async def calc_handler(message: Message) -> None:
    # запрос сюда
    available_specialties = []
    subject_specialties = []
    ANSWER_TEXT = f'''Специальности с вашими экзаменами: {subject_specialties}, 
                      с подходящими баллами: {available_specialties}'''.strip()
    await message.answer(ANSWER_TEXT, keyboard=KEYBOARD)


@bot.on.message()
async def main_handler(message: Message) -> None:
    global subject
    if subject:
        print({"exam": subject, "score": message.text, "id": message.id})
        # запрос сюда
        await subject_handler(message)
    else:
        KEYBOARD = (
            Keyboard(one_time=True)
            .add(Text("Калькулятор ЕГЭ"))
            .add(Text("О боте"))
            .get_json()
        )
        await message.answer('Доступные кнопки', keyboard=KEYBOARD)

uvloop.install()
bot.run_forever()