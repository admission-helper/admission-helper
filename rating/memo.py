import pandas as pd

file_path = 'data/memo.xlsx'
# файл с факультетами, специальностями и информацией о них

bachelor = pd.read_excel(file_path, sheet_name='Бакалавриат и специалитет')
master = pd.read_excel(file_path, sheet_name='Магистратура')
postgraduate = pd.read_excel(file_path, sheet_name='Аспирантура')

def faculties_by_degree(degree):
    return degree['Факультет'].dropna()

def specialties_by_faculty(faculty, degree):
    faculties = degree['Факультет']
    faculties = faculties.fillna(method='ffill', axis=0) # заполнение объединённых ячеек
    fac_specialties = {faculty: []} # словарь с названием факультета
    specialties = degree['Направление подготовки']

    for i in range(len(specialties)):
        if faculties[i] == faculty:
            fac_specialties[faculty].append(specialties[i])

    return fac_specialties

def choose_specialty(fac_specialties, specialty):
    return {list(fac_specialties.keys())[0]: specialty}


#def info_by_specialty(specialty, degree):

specialties = specialties_by_faculty('Математический', bachelor)
print(choose_specialty(specialties, '01.03.02 Прикладная математика и информатика'))