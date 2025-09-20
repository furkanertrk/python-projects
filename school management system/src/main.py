import sqlite3
import os

print(""" Okul Yönetim Sistemine Hoşgeldiniz """)

path = "School\\data\\"
db_name = "school.db"
db_path = os.path.join(path,db_name)
def database_setup():
    if not os.path.exists(path):
        os.makedirs(path)
    db = sqlite3.connect(db_path)
    conn = db.cursor()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS 'SCL_DB' (NAME TEXT, LASTNAME TEXT, AGE INTEGER, GENDER TEXT, STATUS TEXT)")
    db.commit()
    db.close()

def database_add(data):
    db = sqlite3.connect(db_path)
    conn = db.cursor()
    conn.execute("INSERT INTO 'SCL_DB' (NAME, LASTNAME, AGE, GENDER, STATUS) VALUES (?, ?, ?, ?, ?)",
                 (data.name, data.lastname, data.age, data.gender, data.status))
    db.commit()
    db.close()
def database_print_all():
    db = sqlite3.connect(db_path)
    conn = db.cursor()
    conn.execute("SELECT * FROM 'SCL_DB'")
    datas = conn.fetchall()
    if datas:  # Verilerin var olup olmadığını kontrol edin
        for record in datas:
            print(record)
    else:
        print("Veritabanında kayıt bulunamadı.")
    db.close()
def delete_all_db():
    db = sqlite3.connect(db_path)
    conn = db.cursor()
    conn.execute("DELETE FROM 'SCL_DB'")
    db.commit()
    db.close()


class Human:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

class Student(Human):
    def __init__(self, name, lastname,age,gender):
        Human.__init__(self,name,lastname)
        self.age = age
        self.gender = gender
        self.status = "Öğrenci"

class Teacher(Human):
    def __init__(self, name, lastname,age,gender):
        Human.__init__(self,name,lastname)
        self.age = age
        self.gender = gender
        self.status = "Öğretmen"


delete_all_db()
H1 = Student("Furkan","Ertürk",19,"Male")
H2 = Teacher("Berat","Bayram",22,"Male")

temp = [H1,H2]

database_setup()
for i in temp:
    database_add(i)

database_print_all()
