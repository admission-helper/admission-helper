async def add_user(conn, user_id):
    await conn.execute('''call bot.add_user('%s')''' %user_id)
    await conn.commit()
    await conn.close()

async def add_user_req(conn, user_id, exam_name, ball):
    await conn.execute('''call bot.add_user_req('%s','%s',%i::smallint)'''
        % (user_id, exam_name, int(ball)))
    await conn.close()

async def get_pass_directions(conn, user_id):
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
                    u.user_vk_id = '%s') tb
            group by 
                dir_nm, fac_nm
            having 
                sum(tb.ball_qnt) > sum(tb.ball) 
        ''' % user_id)
    return values

async def get_all_directions(conn, user_id):
    values = await conn.fetch('''
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
    await conn.close()
    return values

async def get_all_directions(conn, user_id):

    res = await conn.fetch('''select * from bot.get_all_directions('%s');''' % user_id)

    return res


async def actualize_status(conn, user_id):
    await conn.execute('''call bot.status('%s')''' % user_id)
    