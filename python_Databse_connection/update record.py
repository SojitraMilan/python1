import mysql.connector as con
try:
   mydb = con.connect(host="localhost",user="root",password="",database="python1")

   mycursor= mydb.cursor()
   rno = input("roll no:")

   nm = input("Name:")
   city = input("City:")
   argd=(nm,city,rno)
   sql = "update tb1 set nm=%s,city=%s where id=%s"
   mycursor.execute(sql,argd)
   print("Record Inserted SuccessFullly....")
   mydb.commit()
except:
   print("Error")