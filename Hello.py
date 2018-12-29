import mysql.connector


def saveStudentInDB(sRef):
    sql="insert into Student values(null,'{}','{}')".format(sRef.name,sRef.address)

    con = mysql.connector.connect(user="root",password="", host="localhost",database="Student")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
def UpdateStudentInDB(sRef):
    sql="update Student set name= '{}', address='{}' where roll={})".format(sRef.name,sRef.address,sRef.roll)

    con = mysql.connector.connect(user="root",password="", host="localhost",database="Student")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print(sRef.name, "Updated in DB !!")
def fetchStudentInDB():
    sql="Select * from Student"

    con = mysql.connector.connect(user="root",password="", host="localhost",database="Student")
    cursor = con.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)

def deleteStudentInDB(roll):
    sql="delete from Student where roll={}".format(roll)

    con = mysql.connector.connect(user="root",password="", host="localhost",database="Student")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print(roll)

class Student:
    def __init__(self,roll,name,address):
         self.roll=roll
         self.name=name
         self.address=address
         print("Obj create", id(self))

    def __del__(self):
        print("Obj deleted",id(self))

s1=Student(0,"Sia","Redwood Shores")
s2=Student(0,"Johny","Redwood Shore")
saveStudentInDB(s2)
#deleteStudentInDB(2)
fetchStudentInDB()

