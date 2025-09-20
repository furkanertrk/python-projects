import sqlite3



db = sqlite3.connect("ders.db")
cursor = db.cursor()
cursor.execute("SELECT name from sqlite_master WHERE type = 'table' ")
tables = cursor.fetchall()
for i in tables:
    print(i)
db.commit()
db.close()