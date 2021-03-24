import sqlite3

# Creating user Table
conn = sqlite3.connect('virtual_stratup_portal4.db')
cur = conn.cursor()

cur.execute("CREATE TABLE user (U_ID INTEGER, Role_ID INTEGER, Name VARCHAR(200), Email VARCHAR(200) NOT NULL UNIQUE, Password VARCHAR(50), Address VARCHAR(200), Contact INTEGER, PRIMARY KEY (U_ID), FOREIGN KEY (Role_ID) REFERENCES role(Role_ID) ON DELETE CASCADE);")

cur.execute("CREATE TABLE intern (U_ID INTEGER, Course_enroll VARCHAR(200), FOREIGN KEY (U_ID) REFERENCES user(U_ID) ON DELETE CASCADE);")

cur.execute("CREATE TABLE startup (Startup_ID INTEGER NOT NULL, Title VARCHAR(150), Description VARCHAR(500), Solution TEXT, PRIMARY KEY (Startup_ID));")

cur.execute("CREATE TABLE founder (U_ID INTEGER, Startup_ID INTEGER(11), FOREIGN KEY (U_ID) REFERENCES user(U_ID) ON DELETE CASCADE, FOREIGN KEY (Startup_ID) REFERENCES startup(Startup_ID) ON DELETE CASCADE);")

conn.commit()
conn.close()