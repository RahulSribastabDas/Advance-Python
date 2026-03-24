import mysql.connector as my
mydb=my.connect(host="localhost",user="root",password="Rahul@1002",database="new_db")
db_cursor=mydb.cursor()

#step1: create connection
#print("Connection Created")

#Step2: create database  
'''db_cursor.execute("create database new_db")
print("Database Created")'''

#create table
''''db_cursor.execute("create table emp(id int,name varchar(20))")
print("Table Created")'''

#step 4: show tables
'''db_cursor.execute("show tables")
for i in db_cursor:
    print(i)'''

#step 5: insert data into table
'''db_cursor.execute("insert into emp(id,name)values(%s,%s)",(1,"Rahul")) 
print(db_cursor.rowcount,"data inserted")  '''

#insert multiple data into table
'''db_insert="insert into emp(id,name)values(%s,%s)"
db_value=[(2,"Ashish"),(3,"Rajeev"),(4,"Riya"),(5,"Seeta")]
db_cursor.executemany(db_insert,db_value)
mydb.commit()
print(db_cursor.rowcount,"data inserted")'''

#step 6: read data inside table
'''db_cursor.execute("select * from emp")
db_select=db_cursor.fetchall()
print(db_cursor)'''

db_cursor.execute("select * from emp")
for i in db_cursor.fetchall():
    print(i)
