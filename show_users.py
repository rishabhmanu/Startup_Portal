import sqlite3
con = sqlite3.connect('virtual_stratup_portal4.db')
cursor = con.cursor()
cursor.execute("SELECT * from user")
print(cursor.fetchall())

con.close()