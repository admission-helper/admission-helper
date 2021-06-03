from bd import add_user_req, get_pass_directions
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text
from vkbottle.tools.dev_tools import keyboard
from vkbottle.tools.dev_tools.keyboard.action import Payload
from config import TOKEN
import uvloop

from config import database, user, password, host, port
import asyncpg

bot = Bot(TOKEN)



KEYBOARD = (
    Keyboard(one_time=True)
    .add(Text("Калькулятор ЕГЭ"))
    .add(Text("О боте"))
    .row()
    .add(Text("Задать вопрос"))
    .get_json()
)

subject = ''

@bot.on.message(payload={"subject": "subject"})
async def score_handler(message: Message) -> None:

    global subject
    subject = message.text

    keyboard = Keyboard(one_time=True, inline=False).add(Text("Назад")).get_json()

    await message.answer('Введите баллы', keyboard=keyboard)

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
async def back_subject_handler(message: Message) -> None:

    KEYBOARD = (
        Keyboard(one_time=True)
        .add(Text("Калькулятор ЕГЭ"))
        .add(Text("О боте"))
        .row()
        .add(Text("Задать вопрос"))
        .get_json()
    )

    await message.answer('Я вас категорически приветствую', keyboard=KEYBOARD)

@bot.on.message(payload={"subject": "next"})
async def calc_handler(message: Message) -> None:

    conn = await asyncpg.connect(user=user, password=password,
                                    database=database, host=host)

    available_specialties = await get_pass_directions(conn, message.id)
    
    # subject_specialties = []
    # с вашими экзаменами: {subject_specialties}, 
    if available_specialties:
        ANSWER_TEXT = f'Специальности с подходящими баллами: {available_specialties}'
    else:
        ANSWER_TEXT = 'Специальности с подходящими баллами не найдены'
    await message.answer(ANSWER_TEXT, keyboard=KEYBOARD)


@bot.on.message()
async def main_handler(message: Message) -> None:
    global subject
    if subject and message.text != 'Назад':
        # print({"exam": subject, "score": message.text, "id": message.id})

        conn = await asyncpg.connect(user=user, password=password,
                                    database=database, host=host)
        await add_user_req(conn=conn, user_id=message.id, exam_name=subject, ball=message.text)
        
        await subject_handler(message)
    else:
        ANSWER = 'Здесь вы можете задать свой вопрос'
        KEYBOARD = (
            Keyboard(one_time=True)
            .add(Text("Назад", {"subject": "back"}))
            .get_json()
        )
        await message.answer(ANSWER, keyboard=KEYBOARD)

uvloop.install()
bot.run_forever()