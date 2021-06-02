import pandas as pd

file_path = 'data/specialties.xlsx'

bachelor = pd.read_excel(file_path, sheet_name='Бакалавриат и специалитет')

def faculties_by_degree(degree):
    return degree['Наименование факультета'].dropna()

def specialties_by_faculty(faculty, degree):
    faculties = degree['Наименование факультета']
    # faculties = faculties.fillna(method='ffill', axis=0) # заполнение объединённых ячеек
    fac_specialties = [] # словарь с названием факультета
    specialties = degree['Наименование направления подготовки']

    # print(specialties)

    for i, specialty in enumerate(specialties):
        # print(faculties[i], faculty)
        if faculties[i].strip() == faculty.strip():
            fac_specialties.append(specialty.replace('\xa0',''))

    return fac_specialties

def choose_specialty(fac_specialties, specialty):
    return {list(fac_specialties.keys())[0]: specialty}



specialties = specialties_by_faculty('Математический', bachelor)
faculties = faculties_by_degree(bachelor)
a = {}
faculties = [faculty.replace('\xa0','') for faculty in set(faculties)]
for faculty in faculties:
    a[faculty] = specialties_by_faculty(faculty, bachelor)

print(a)

