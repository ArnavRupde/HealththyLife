import sqlite3
from datetime import date, datetime

today = date.today()
conn = sqlite3.connect('faqs.db')
print("Opened database successfully")
usr='Arnav'
pwd='ArnavRupde'
#conn.execute('CREATE TABLE faq (question TEXT, answer TEXT, type TEXT)')
#print("Table created successfully")

#conn.execute('''INSERT INTO patients VALUES (?,?,?,?,?,?,?)''',(usr,pwd))


cursor = conn.cursor()
cursor.execute("INSERT INTO patients (question) \
      VALUES (1,'Ar','Arnav',?,'Cold','Disprine',0.9)",(today));
conn.commit()

##
##c = conn.cursor()
##c.execute('''INSERT INTO patients (pid,password,pname,visit,health,medication,value) VALUES(?,?,?,?,?,?,?)''', (2,'Rj','Raj',today,'Cough','Cough Syrup',0.95))
##conn.commit()


##cur = conn.cursor()
##cur.execute("SELECT * FROM patients")
## 
##rows = cur.fetchall()
## 
##for row in rows:
##    print(row)


conn.close()
