import pandas as pd   # pip install pandas

bachelor = pd.read_excel(r'memo.xlsx', sheet_name='Бакалавриат и специалитет')
undergraduate = pd.read_excel(r'memo.xlsx', sheet_name='Магистратура')
graduate = pd.read_excel(r'memo.xlsx', sheet_name='Аспирантура')


def count(number):
    direction = bachelor['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    number_of_seats = bachelor["План приёма (бюджет) 2020г."].tolist()
    return number_of_seats[index]


def score(number):
    direction = bachelor['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    passing_score = bachelor["Проходной балл 2019г."].tolist()
    return passing_score[index]


def price(number):
    direction = bachelor['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    rubbles = bachelor["Стоимость 2019г. (руб. за год)"].tolist()
    return rubbles[index]


def exams_bachelor(number):
    direction = bachelor['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    exam_bachelor = bachelor["Вступительные испытания (ЕГЭ)"].tolist()
    return exam_bachelor[index]


def focuses_undergraduate(number):
    direction = undergraduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    focus_undergraduate = undergraduate["Наименование направленности"].tolist()
    return focus_undergraduate[index]


def numbers1_undergraduate(number):
    direction = undergraduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    number1_undergraduate = undergraduate["КЦП бюджет"].tolist()
    return number1_undergraduate[index]


def numbers2_undergraduate(number):
    direction = undergraduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    number2_undergraduate = undergraduate["КЦП целевые места"].tolist()
    return number2_undergraduate[index]


def numbers3_undergraduate(number):
    direction = undergraduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    number3_undergraduate = bachelor["КЦП внебюджет"].tolist()
    return number3_undergraduate[index]


def exams_undergraduate(number):
    direction = undergraduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    exam_undergraduate = bachelor["Вступительное испытание"].tolist()
    return exam_undergraduate[index]


def focuses_graduate(number):
    direction = graduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    focus_graduate = undergraduate["Наименование направленности"].tolist()
    return focus_graduate[index]


def numbers1_graduate(number):
    direction = graduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    number1_graduate = undergraduate["КЦП бюджет"].tolist()
    return number1_graduate[index]


def numbers2_graduate(number):
    direction = graduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    number2_graduate = undergraduate["КЦП целевые места"].tolist()
    return number2_graduate[index]


def numbers3_graduate(number):
    direction = graduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    number3_graduate = bachelor["КЦП внебюджет"].tolist()
    return number3_graduate[index]


def exams_graduate(number):
    direction = graduate['Направление подготовки'].tolist()
    for i in range(len(direction)):
        direction[i] = direction[i][:8]
    index = direction.index(number)
    exam_graduate = bachelor["Вступительное испытание"].tolist()
    return exam_graduate[index]