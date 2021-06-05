import asyncio
from bd import actualize_status, add_user_req
import asyncpg
from config import user, password, database, host

async def main():
    conn = await asyncpg.connect(user=user, password=password,
                                        database=database, host=host)
    user_id = 1
    # await add_user_req(conn=conn, user_id=user_id, exam_name='Русский', ball='100')
    # await add_user_req(conn=conn, user_id=user_id, exam_name='Биология', ball='100')
    # await add_user_req(conn=conn, user_id=user_id, exam_name='Химия', ball='100')

    # await actualize_status(conn, user_id)

    # values = await conn.fetch('''
    # select distinct 
    #         dir_nm, 
    #         fac_nm
    #     from
    #         (select * from bot.user_requests ur 
    #             join bot.exams e on e.id_exam = ur.id_exam 
    #             join bot.directions_exams de on e.id_exam = de.id_exam 
    #             join bot.directions d on d.id_direction = de.id_direction 
    #             join bot.faculty f on f.id_fac = d.id_fac 
    #             join bot.admission_scores ass on ass.id_de = de.id_de 
    #             join bot.calendar c on ass.id_year = c.id_note
    #             join bot.users u on u.id_user = ur.id_user
    #         where 
    #             u.user_vk_id = '%s') tb
    # ''' % user_id)
    # await conn.close()
    # print(values)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())