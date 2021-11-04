from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

base = Tk()
base.geometry("800x700")
base.title("Student Details ")
base.configure(bg="#F5FFFA")

f = ("Arial Bold",20)

def submit():
    s1 = t1.get()
    s2 = int(t2.get())
    s3 = t3.get()
    s4 = str(c1.get())
    s5 = int(t5.get())
    s6 = t6.get()
    con = sqlite3.connect("student_info.db")
    query = f"insert into student_details values({s2},'{s1}','{s6}',{s5},'{s4}','{s3}')"
    con.execute(query)
    con.commit()
    con.close()
    messagebox.showinfo("Add data successfully", "saved data successfully....")
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t6.delete(0, END)
    t5.delete(0, END)


def reset():
    t1.delete(0,END)
    t2.delete(0, END)
    t3.delete(0, END)
    t6.delete(0, END)
    t5.delete(0, END)



l = Label(base,text="Insert Student Details ",font=("Arial Bold",35),bg="#F5FFFA",bd=10)
l.place(x=180,y=30)

l1 = Label(base,text="Student Name : -",font=f,bg="#F5FFFA",)
l1.place(x=70,y=150)

t1 = Entry(base,width=25,font=f,bd=5)
t1.place(x=340,y=150)

l2 = Label(base,text="Student Roll No : -",font=f,bg="#F5FFFA",)
l2.place(x=70,y=220)

t2 = Entry(base,width=25,font=f,bd=5)
t2.place(x=340,y=220)

l3 = Label(base,text="Student Class : -",font=f,bg="#F5FFFA",)
l3.place(x=70,y=290)

t3 = Entry(base,width=25,font=f,bd=5)
t3.place(x=340,y=290)

l4 = Label(base,text="Select Branch : -",font=f,bg="#F5FFFA",)
l4.place(x=70,y=360)

branch = ["Computer Engg","Information Tech","Electronics Engg","Mechanical Engg","Civil Engg"]
c1 = ttk.Combobox(base,values=branch,font=f,state="readonly",width=24)
c1.place(x=340,y=360)

l5 = Label(base,text="Phone No : -",font=f,bg="#F5FFFA",)
l5.place(x=70,y=430)

t5 = Entry(base,width=25,font=f,bd=5)
t5.place(x=340,y=430)

l6 = Label(base,text="Student City : -",font=f,bg="#F5FFFA",)
l6.place(x=70,y=500)

t6 = Entry(base,width=25,font=f,bd=5)
t6.place(x=340,y=500)

b1 = Button(base,text="Submit",font=f,bg="#1E90FF",bd=5,width=10,command=submit)
b1.place(x=150,y=600)

b2 = Button(base,text="Reset",font=f,bg="#1E90FF",bd=5,width=10,command=reset)
b2.place(x=450,y=600)
base.mainloop()