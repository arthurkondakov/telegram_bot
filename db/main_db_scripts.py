from config import db, cursor

def enter_user_info(user_id, first_name, last_name, username, start_date):
    cursor.execute(f"""INSERT INTO 'users' (
                   user_id,
                   first_name,
                   last_name,
                   username,
                   start_date) VALUES (
                   {user_id},
                   '{first_name}',
                   '{last_name}',
                   '{username}',
                   {start_date} )
                """)
    db.commit()