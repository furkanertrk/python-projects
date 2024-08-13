import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id integer PRIMARY KEY,
        name text,
        lastname text,
        username text,
        password text
    )""")
    conn.commit()
    conn.close()

def insert(name,lastname,username,password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    add_command = """ INSERT INTO USERS (name,lastname,username,password) VALUES {}"""
    data = (name,lastname,username,password)
    cursor.execute(add_command.format(data))
    conn.commit()
    conn.close()

def search_user(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    search_command = """ SELECT * from USERS WHERE username = '{}' """
    cursor.execute(search_command.format(username))
    user = cursor.fetchone()
    conn.close()
    return user


def print_all():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name,lastname,username FROM USERS")
    list_all = cursor.fetchall()
    for i in list_all:
        print(i)
    conn.close()

def password_update(username,newPassword):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    upt_command = """ UPDATE USERS SET password = '{}' WHERE username = '{}' """
    cursor.execute(upt_command.format(username,newPassword))
    conn.commit()
    conn.close()

def delete_account(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    delete_command = """ DELETE from USERS WHERE username = '{}' """
    cursor.execute(delete_command.format(username))
    conn.commit()
    conn.close()

def _delete_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    delete_command = """ DROP TABLE USERS"""
    cursor.execute(delete_command)
    conn.commit()
    conn.close()
