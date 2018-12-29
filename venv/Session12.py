from tkinter import *
import mysql.connector

entryName = None
entryPhone = None
entryPoint = None
name1= None
updatedpoint1 = None
user1= None


class Customer:
    def __init__(self,name,phone,point,user):
        self.name=name
        self.phone=phone
        self.point=point
        self.user=user

    def __del__(self):
        print("Object deleted")

def saveCustomerInDB(cRef):
             # Create SQL Query
    sql = "insert into Customer values(null, '{}', '{}', '{}','{}')".format(cRef.name, cRef.phone, cRef.point,cRef.user)

             # Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")

             # Execute SQL Query On Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print("Customer", cRef.name, " Registered in Loyalty Program !!")
def fetchfromDB():
    sql="Select * from Customer"

    con = mysql.connector.connect(user="root",password="", host="localhost",database="Student")
    cursor = con.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    print(rows)
    String =str(rows)
    print(String)
    print(type(String))
    # for row in rows:
    #     print(row)
    # point1 = ' '.join(rows)
    # print(point1)
    # print(type(point1))
    newwin = Tk()
    lblText = Label(newwin, text=String)
    lblText.pack()
    # entryName = Entry(window)
    # entryName.pack()

def deactivateDB(cRef):
    sql = "update Customer set user='{}' where phone='{}'".format(cRef.user, cRef.phone)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="Student")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

def UpdateStudentInDB(cRef):
    sql="update Customer set name= '{}', point='{}' where phone='{}'".format(cRef.name,cRef.point,cRef.phone)

    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print(cRef.name, "Updated in DB !!")
def RedeemDB(cRef):
    sql="update Customer set point= '{}' where phone='{}'".format(cRef.point,cRef.phone)

    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
def AddPointDB(cRef):
    global updatedpoint1
    sql = "Select point from Customer  where phone= {}".format(cRef.phone)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
    cursor = con.cursor()
    cursor.execute(sql)
    updatedpoint1= cursor.fetchone()
    point1=updatedpoint1[0]
    print(point1)
    print(type(point1))
    cRef.point = point1+cRef.point
    print(cRef.point)
    sql = "update Customer set point = '{}' where phone= {}".format(cRef.point, cRef.phone)

    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Points added")

def Redeem():
    phone2=entryPhone.get()
    point2=0
    cRef = Customer(name1, phone2, point2, user1)
    RedeemDB(cRef)
def onClick():
    print("Button Clicked")

    name = entryName.get()

    phone = entryPhone.get()

    point= float(entryPoint.get())
    updatedpoint = point/100
    user= 1
    cRef = Customer(name, phone, updatedpoint,user)
    print(cRef.__dict__)

    saveCustomerInDB(cRef)
    entryName.delete(0,END)
    entryPhone.delete(0, END)
    entryPoint.delete(0, END)
def Update():
    #showWindow()
    global name1
    global updatedpoint1
    name1 = entryName.get()
    phone1 = entryPhone.get()
    point1 = float(entryPoint.get())
    updatedpoint1 = point1/100
    user1 = 1
    cRef = Customer(name1, phone1, updatedpoint1,user1)
    UpdateStudentInDB(cRef)
    entryName.delete(0, END)
    entryPhone.delete(0, END)
    entryPoint.delete(0, END)
def deactivate():
    phone2 = entryPhone.get()
    user2= 0
    cRef = Customer(name1,phone2,updatedpoint1, user2)
    print(cRef.__dict__)
    deactivateDB(cRef)
    print()
    entryName.delete(0, END)
    entryPhone.delete(0, END)
    entryPoint.delete(0, END)
def AddPoint():
    phone2 = entryPhone.get()
    point2 = float(entryPoint.get())
    updatedpoint2 = point2 / 100
    cRef = Customer(name1,phone2,updatedpoint2, user1)
    AddPointDB(cRef)
def mhello1():

    newwin = Tk()



def showWindow():

    global entryName
    global entryPhone
    global entryPoint
    global btnAddCustomer

    window = Tk()
    lblTitle = Label(window, text="Add Your Customer Details")
    lblTitle.pack()

    lblName = Label(window, text="Add Your Customer name")
    lblName.pack()

    entryName = Entry(window)
    entryName.pack()

    lblPhone = Label(window, text="Add Your Customer phone")
    lblPhone.pack()

    entryPhone = Entry(window)
    entryPhone.pack()

    lblPoint= Label(window, text="Enter your Purchasing amount")
    lblPoint.pack()

    entryPoint = Entry(window)
    entryPoint.pack()


    btnAddCustomer= Button(window,text="Add Customer",command= onClick)
    btnAddCustomer.pack()

    btnNext= Button(window,text="Second Activity",command=mhello1)
    btnNext.pack()

    btnUpdateCustomer = Button(window, text="Update Customer", command= Update)
    btnUpdateCustomer.pack()

    btnfetchCustomer = Button(window, text="Fetch Customer",command= fetchfromDB)
    btnfetchCustomer.pack()

    btnDeActivateCustomer = Button(window, text="DeActivate Customer",command = deactivate)
    btnDeActivateCustomer.pack()

    btnRedeemCustomer = Button(window, text="Reedem Points",command = Redeem)
    btnRedeemCustomer.pack()

    btnAddPointCustomer = Button(window, text="Add Points",command = AddPoint)
    btnAddPointCustomer.pack()
    window.mainloop()

showWindow()