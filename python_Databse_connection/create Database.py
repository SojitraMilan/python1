import mysql.connector

mydb= mysql.connector.connect(host = "localhost",user = "root",password="")

mycurrsor = mydb.cursor();
mycurrsor.execute("Create Database python1")
print("Database Created sucessfully.....")