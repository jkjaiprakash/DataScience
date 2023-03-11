### GUI(Graphical User Interface)
###tkinter is used to interface to man to system.
###tkinter is inbuilt library
##
##
####import tkinter
####from tkinter import filedialog
####root=tkinter.Tk()  #root dialouge box vachi than main dialouge box create panna
####var=filedialog.askdirectory()
####filename='best.txt'
####path=var+'/'+filename
####var1=open(path,'w')
####var1.write('hello')
####var1.close()
##
##
####import os
####import tkinter
####from tkinter import filedialog
####from tkinter import messagebox
####root=tkinter.Tk()
####root.withdraw()
####var=filedialog.askdirectory()
####filename='best2.txt'
####path=os.path.join(var,filename)
####var1=open(path,'w')
####var1.write('you r the best')
####var1.close()
####messagebox.showinfo(path,'suresh')
##
##import tkinter
##from tkinter import messagebox
##from tkinter import*
##import sqlite3
##root=tkinter.Tk()
##def submit():
##    conn=sqlite3.connect('new.db')
##    cursor=conn.cursor()
##    cursor.execute("insert into form values(:name,:age,:gender,:mail)",
##    {
##        'name':name_entry.get(),
##        'age':age_entry.get(),
##        'gender':gender_entry.get(),
##        'mail':mail_entry.get()
##        }
##    )
##    name_entry.delete(0,END)
##    age_entry.delete(0,END)
##    gender_entry.delete(0,END)
##    mail_entry.delete(0,END)
##    conn.commit()
##    conn.close()
##def check():
##    conn=sqlite3.connect('new.db')
##    cursor=conn.cursor()
##    cursor.execute('select * from form where name=? AND age=? AND gender=?',(name_entry.get(),age_entry.get(),gender_entry.get()))
##    data=cursor.fetchone()
##    if data:
##        messagebox.showinfo('message','user already exists')
##    else:
##        messagebox.showinfo('message','no user pannel')
##    conn.commit()
##    conn.close()
##    
##root.title('login')
##root.geometry('200x300')
##age_entry=StringVar()
##name_entry=StringVar()
##gender_entry=StringVar()
##name=Label(root,text='NAME')
##name.grid(row=0,column=0)  #grid means which locate to
##name_entry=Entry(root)
##name_entry.grid(row=0,column=1)
##
##age=Label(root,text='AGE')
##age.grid(row=1,column=0)
##age_entry=Entry(root)
##age_entry.grid(row=1,column=1)
##
##gender=Label(root,text='GENDER')
##gender.grid(row=3,column=0)
##gender_entry=Entry(root)
##gender_entry.grid(row=3,column=1)
##
##mail=Label(root,text='MAIL ID')
##mail.grid(row=4,column=0)
##mail_entry=Entry(root)
##mail_entry.grid(row=4,column=1)
##
##submit=Button(root,text='SUBMIT',command=submit)
##submit.grid(row=5,column=0)
##
##check=Button(root,text='CHECK',command=check)
##check.grid(row=5,column=1)
##cancel=Button(root,text='CANCEL',command=root.destroy)
##cancel.grid(row=5,column=2)
##
####conn=sqlite3.connect('new.db')
####cursor=conn.cursor()
####cursor.execute("create table form(name text,age int,gender text,mail text)")
####conn.commit()
####conn.close()
##
##
##
####import tkinter
####from tkinter import*
####root=tkinter.Tk()
####root.title('login')
####root.geometry('300x200')
####
####name=Label(root,text='NAME')
####name.grid(row=0,column=0)  #grid means which locate to
####name_entry=Entry(root)
####name_entry.grid(row=0,column=1)
####
####age=Label(root,text='AGE')
####age.grid(row=1,column=0)
####age_entry=Entry(root)
####age_entry.grid(row=1,column=1)
####
####gender=Label(root,text='GENDER')
####gender.grid(row=3,column=0)
####gender_entry=Entry(root)
####gender_entry.grid(row=3,column=1)
####
####mail=Label(root,text='MAIL ID')
####mail.grid(row=4,column=0)
####mail_entry=Entry(root)
####mail_entry.grid(row=4,column=1)
####
####submit=Button(root,text='SUBMIT')
####submit.grid(row=5,column=0)
####
####check=Button(root,text='CHECK')
####check.grid(row=5,column=1)
####
####cancel=Button(root,text='CANCEL')
####cancel.grid(row=5,column=2)
##
##
##
##
##
##
##
##
##
##
##
##
