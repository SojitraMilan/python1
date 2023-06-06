import mysql.connector as con
try:
    mydb = con.connect(host = "localhost",user = "root",password='',database='python1')
  
 
    mycursor = mydb.cursor()
    id = input("Roll No:")
    nm = input("Name:")
    city = input("city:")

    args = (id,nm,city) 
    mycursor.execute("insert into tb1 values(%s,%s,%s)",args)
    print("Record inserted SuccsessFully...")
    mydb.commit()
except:
    print("error")
