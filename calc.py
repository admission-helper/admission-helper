import pandas as pd


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



# specialties = specialties_by_faculty('Математический', bachelor)
# faculties = faculties_by_degree(bachelor)
# a = {}
# faculties = [faculty.replace('\xa0','') for faculty in set(faculties)]
# for faculty in faculties:
#     a[faculty] = specialties_by_faculty(faculty, bachelor)

# print(a)



# print(bachelor['Наименование факультета'].unique())
# print(bachelor['Наименование факультета'])


# a = dict.fromkeys(('Биология', 'Химия'))
# print(a)
def possible_specialties(exams) -> dict:
    specialties = {}
    file_path = 'data/specialties.csv'
    bachelor = pd.read_csv(file_path)
    poss_exams = (bachelor['Вступительное испытание 1'], 
                bachelor['Вступительное испытание 2_1'], 
                bachelor['Вступительное испытание 2_2'])
    for i, item in enumerate(zip(*poss_exams)):
        if item[0] in exams:
            if item[1] in exams or item[2] in exams:
                specialties[bachelor['Наименование факультета'][i]] = specialties.get(bachelor['Наименование факультета'][i], [])
                specialties[bachelor['Наименование факультета'][i]].append({
                           'Специальность': bachelor['Наименование направления подготовки'][i],
                           'Профиль': bachelor['Наименование направленности (профиля)'][i]})
    return specialties

# print(bachelor.loc[bachelor['Вступительное испытание 1'] == 'Математика'].values)
# dict from keys