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

    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)

    values = await conn.fetch(f'''
    select distinct 
            dir_nm, 
            fac_nm
        from
            (select * from bot.user_requests ur 
                join bot.exams e on e.id_exam = ur.id_exam 
                join bot.directions_exams de on e.id_exam = de.id_exam 
                join bot.directions d on d.id_direction = de.id_direction 
                join bot.faculty f on f.id_fac = d.id_fac 
                join bot.admission_scores ass on ass.id_de = de.id_de 
                join bot.calendar c on ass.id_year = c.id_note
                join bot.users u on u.id_user = ur.id_user
            where 
                u.user_vk_id = '{message.id}') tb
        group by 
            dir_nm, fac_nm
        having 
            sum(tb.ball_qnt) > sum(tb.ball) 
    '''
        )
    await conn.close()
    print(values)

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
        # print({"exam": subject, "score": message.text, "id": message.id})
        # cursor = conn.cursor()
        # add_user_req(user_id=message.id, exam_name=subject, ball=message.text)

        # cursor.execute('''call bot.add_user_req('%s','%s',%i::smallint)'''
                # % (message.id, subject, int(message.text)))
        
        print(values)
        conn.commit()
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