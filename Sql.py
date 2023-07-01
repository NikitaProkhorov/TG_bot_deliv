import sqlite3

async def db_start():
    global db, cur 

    db = sqlite3.connect('bot.db')
    cur = db.cursor()


async def logg(user_id, user_name, user_surname, bonus, time):
    user = cur.execute("SELECT 1 FROM users WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", (user_id, user_name, user_surname, bonus, time))
        db.commit()