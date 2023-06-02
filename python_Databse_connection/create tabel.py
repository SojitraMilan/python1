import mysql.connector

mydb = mysql.connector.connect(host= "localhost",user="root",password="",database='python1')

mycursor = mydb.cursor()
mycursor.execute("create table tb1(id int(11),nm varchar(20),city varchar(10))")
print("tabel created successfully....")