import mysql.connector as con

mydb = con.connect(host="localhost",user="root",password='',database="python1")

mycursor=mydb.cursor()
rno = input("Roll no:")
args = (rno,)
sql = "delete from tb1 where id=%s"
mycursor.execute(sql,args)
print("Record Deleted SuccsesFullyy....")
mydb.commit()