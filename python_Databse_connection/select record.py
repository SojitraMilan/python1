import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user="root",password="",database='python1')

mycursor = mydb.cursor()
mycursor.execute("select * from tb1")
rows = mycursor.fetchall()
for row in rows:
    print(row[0],"\t",row[1],"\t",row[2])
mydb.commit()