import sqlite3

conn = sqlite3.connect('veritabani.db')

cursor = conn.cursor()
cursor.execute("""SELECT * FROM 'tablo_adi' WHERE Gender == "Male" AND [Job Title]=='Senior Engineer' """)
veriler=cursor.fetchall()  #verileri yazdırmak için
for a in veriler:
    print(a)

conn.close()