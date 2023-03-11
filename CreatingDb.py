##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##cursor.execute("create table beasant(id int,name text,ag int)")
##Connection.commit()
##Connection.close()

##import sqlite3
##Connection=sqlite3.connect("Employee.db")
##cursor=Connection.cursor()
##cursor.execute("create table beasant(ID int,name text,ag int)")
##Connection.commit()
##Connection.close()


##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##cursor.execute("insert into  beasant(id,name,ag)values(1,'dhoni',40),(2,'virat',35),(3,'Yuvi',45)")
##Connection.commit()
##Connection.close()

##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##query=cursor.execute("Select ag from beasant where name='dhoni'")
##data=cursor.fetchall()
##print(data)
##Connection.commit()
##Connection.close()

##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##query=cursor.execute("Select * from beasant where name='dhoni'")
##data=cursor.fetchall()
##print(data)
##Connection.commit()
##Connection.close()

##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##query=cursor.execute("update beasant set ag=42 where name='dhoni'")
##Connection.commit()
##Connection.close()


##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##query=cursor.execute("update beasant set ag=42 where name='dhoni'")
##Connection.commit()
##Connection.close()


##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##cursor.execute("alter table beasant add column 'Gender'")
##Connection.commit()
##Connection.close()

##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##cursor.execute("update beasant set Gender='Male' where id=1")
##Connection.commit()
##Connection.close()

##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##cursor.execute("alter table beasant rename to Tech")
##Connection.commit()
##Connection.close()

##import sqlite3
##Connection=sqlite3.connect("Sample.db")
##cursor=Connection.cursor()
##cursor.execute("delete from Tech where id=1")
##Connection.commit()
##Connection.close()

