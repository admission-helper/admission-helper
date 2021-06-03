from os import pread
import psycopg2

from config import database, user, password, host, port


conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

def add_user(user_id):
    cursor.execute('''call bot.add_user('%s')''' %user_id)
    conn.commit()

def add_user_req(user_id, exam_name, ball):
    cursor.execute('''call bot.add_user_req('%s','%s',%i::smallint)'''
        % (user_id, exam_name, int(ball)))
    conn.commit()


def get_pass_directions(user_id):
    cursor.execute('''
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
                u.user_vk_id = '%s') tb
        group by 
            dir_nm, fac_nm
        having 
            sum(tb.ball_qnt) > sum(tb.ball) 
    ''' % user_id)
    return cursor.fetchall()


def get_all_directions(user_id):
    cursor.execute('''
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
                u.user_vk_id = '%s') tb
    ''' % user_id)
    return cursor.fetchall()

add_user_req(user_id=1, exam_name='Жопа ахаха', ball='0')