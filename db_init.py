import sqlite3

conn = sqlite3.connect('virtual_stratup_portal4.db')


conn.execute("CREATE TABLE role (Role_ID INT, Role_Name VARCHAR(100), PRIMARY KEY (Role_ID))")
cur = conn.cursor()
cur.execute("INSERT INTO role VALUES ('1', 'Founder'),('2', 'Intern')")
conn.commit()
conn.close()

