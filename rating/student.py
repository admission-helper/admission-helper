import pandas as pd

df = pd.read_excel(r'students.xlsx', sheet=0)
# print(df)

class Student:
    def __init__(self, name, index, rating):
        self.name = name
        self.index = index
        self.rating = rating

        #self.diploma

    def print_info(self):
        info = 'ФИО: ' + self.name + '\nМесто в рейтинге: ' + self.rating
        return info
        # print('Оригинал аттестата: ' + self.diploma)


def find_index(student_name):
    name = df['Имя'].tolist()
    for i in range(len(name)):
        name[i] = name[i].lower()
    index = name.index(student_name)
    return index + 1


def info_by_index(index):
    # summary = []

    # exam = df['Баллы ЕГЭ'][index]
    # additional = df['Доп. Баллы'][index]
    # sum_points = df['Суммарно'][index]

    originals = df['Оригинал аттестата'].tolist()
    # original = originals[index]
    count = (len(originals))

    position = str(index) + '/' + str(count)

    # summary.append(exam)
    # summary = [student, position, original]

    return position


def full_info(name):
    try:
        index = find_index(name)
        rating = info_by_index(index)
        student = Student(name, index, rating)
        return student.print_info()
    except:
        return 'Имя не в списке'


def number_of_seats():
    number = (len(df['Оригинал аттестата'].tolist()))
    return number

# print(full_info('Студент 1'))

# print_info(summary)