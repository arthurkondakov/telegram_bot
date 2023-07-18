from config import db, cursor


def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'users'(
                   user_id INTEGER,
                   first_name TEXT,
                   last_name TEXT,
                   username TEXT,
                   start_date INTEGER);
                   """)
    db.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 'form_info'(
                    user_id INTEGER,
                    user_name TEXT,
                    age_user INTEGER,
                    phone_user INTEGER,
                    city_user TEXT)
                    """)
    db.commit()

