##  ==================          GUI     ===================================##

##import tkinter
##root=tkinter.Tk()

##import tkinter
##from tkinter import filedialog
##root=tkinter.Tk()
##var=filedialog.askdirectory()
##filename="Samplle.txt"
##filepath=var+"/"+filename
##var1=open(filepath,"w")
##var1.write("Hello")
##var1.close()

##import os
##import tkinter
##from tkinter import filedialog
##from tkinter import messagebox
##root=tkinter.Tk()
##root.withdraw()
##var=filedialog.askdirectory()
##filename="Sample.txt"
##filepath=os.path.join(var,filename)
##var1=open(filepath,"w")
##var1.write("Hello")
##var1.close()
##messagebox.showinfo("mybox",filepath)

##import tkinter
##root=tkinter.Tk()
##root.title('Login Page')
##root.geometry('600x400')


##import tkinter
##from tkinter import *
##root=tkinter.Tk()
##root.title('Login Page')
##root.geometry('600x400')
##Name=Label(root,text="Name")
##Name.grid(row=0,column=0)
##Age=Label(root,text="Age")
##Age.grid(row=1,column=0)
##Gender=Label(root,text="Gender")
##Gender.grid(row=2,column=0)
##Occupation=Label(root,text="Occupation")
##Occupation.grid(row=3,column=0)
##Name_entry=Entry(root,width=30)
##Name_entry.grid(row=0,column=2)
##Age_entry=Entry(root,width=30)
##Age_entry.grid(row=1,column=2)
##Gender_entry=Entry(root,width=30)
##Gender_entry.grid(row=2,column=2)
##Occupation_entry=Entry(root,width=30)
##Occupation_entry.grid(row=3,column=2)
##Submit=Button(root,text="Submit")
##Submit.grid(row=4,column=0)
##Check=Button(root,text="Check")
##Check.grid(row=4,column=2)
##Cancel=Button(root,text="Cancel",command=root.destroy)
##Cancel.grid(row=4,column=5)

import sqlite3
import tkinter
from tkinter import *
root=tkinter.Tk()
root.title('Login Page')
root.geometry('600x400')
Name=Label(root,text="Name")
Name.grid(row=0,column=0)
Age=Label(root,text="Age")
Age.grid(row=1,column=0)
Gender=Label(root,text="Gender")
Gender.grid(row=2,column=0)
Occupation=Label(root,text="Occupation")
Occupation.grid(row=3,column=0)
Name_entry=Entry(root,width=30)
Name_entry.grid(row=0,column=2)
Age_entry=Entry(root,width=30)
Age_entry.grid(row=1,column=2)
Gender_entry=Entry(root,width=30)
Gender_entry.grid(row=2,column=2)
Occupation_entry=Entry(root,width=30)
Occupation_entry.grid(row=3,column=2)
Submit=Button(root,text="Submit")
Submit.grid(row=4,column=0)
def fun():
    Connection=sqlite3.connect("Sample.db")
    cursor=Connection.cursor()
    query=cursor.execute("update Firstdata where Summit=input()")
    Connection.commit()
    Connection.close()
Connection=sqlite3.connect("Databaseupdation.db")
cursor=Connection.cursor()
cursor.execute("create table Firstdata(id int,name text,ag int,Occupation text)")
Connection.commit()
Connection.close()
Summit=Button(root,text="Submit",command=root.fun())
Check=Button(root,text="Check")
Check.grid(row=4,column=2)
Cancel=Button(root,text="Cancel",command=root.destroy)
Cancel.grid(row=4,column=5)
