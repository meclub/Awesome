import sqlite3

conn = sqlite3.connect("test.db")
print("open sqlite success")

c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INTEGER PRIMARY KEY     ,
       NAME           TEXT    NOT NULL,
       ADD_TIME       TEXT     NOT NULL,
       SUB_TYPE         CHAR(50),
       SALARY         REAL);''')
print("Table created successfully")
conn.commit()

c.execute("INSERT INTO COMPANY (NAME, ADD_TIME, SUB_TYPE, SALARY) \
      VALUES ('Paul', '1591326559111', '310303', 20000.00 )")

c.execute("INSERT INTO COMPANY (NAME, ADD_TIME, SUB_TYPE, SALARY) \
      VALUES ('Allen', '1591326559112', '310304', 15000.00 )")

c.execute("INSERT INTO COMPANY (NAME, ADD_TIME, SUB_TYPE, SALARY) \
      VALUES ('Teddy', '1591326559113', '310305', 20000.00 )")

c.execute("INSERT INTO COMPANY (NAME, ADD_TIME, SUB_TYPE, SALARY) \
      VALUES ('Mark', '1591326559114','310306 ', 65000.00 )")
print("Records created successfully")
conn.commit()

cursor = c.execute("SELECT id, name, add_time, salary  from COMPANY")
# SELECT DATE_FORMAT(add_time,'%y-%m-%d')
cursor.__sizeof__()
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")