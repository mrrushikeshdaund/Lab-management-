from tkinter import *
from tkinter import messagebox
import random
def changepassword():
    w = Tk()
    w.title("Reset Password page")
    w.geometry("700x700")
    w.configure(bg="#F5FFFA")

    def sendotp():
        a = random.randint(0000,9999)
        messagebox.showinfo("Message send to phone","one time  password is "+str(a)+" do share anyone it validate for 10 mins ")



    def enter2(event):
        l3.configure(fg="#1E90FF")

    def leave2(event):
        l3.configure(fg="Black")

    f = ("Arial Bold", 20)
    l1 = Label(w, text="Enter User ID", font=f, bg="#F5FFFA", bd=3)
    l1.place(x=20, y=20)

    t1 = Entry(w, width=17, font=f, bd=5)
    t1.place(x=290, y=20)

    b1 = Button(w, text="Send OTP", font=f, bg="#1E90FF", bd=3, width=10,command=sendotp)
    b1.place(x=200, y=90)

    l2 = Label(w, text="Enter OTP", font=f, bg="#F5FFFA", bd=3)
    l2.place(x=20, y=180)

    t2 = Entry(w, width=10, font=f, bd=5, show='*')
    t2.place(x=220, y=180)

    l3 = Label(w, text="Verify OTP", font=("Arial Bold", 12), bg="#F5FFFA")
    l3.bind('<Enter>', enter2)
    l3.bind('<Leave>', leave2)
    l3.place(x=390, y=190)

    l4 = Label(w, text="Enter Password ", font=f, bg="#F5FFFA", bd=3)
    l4.place(x=20, y=290)

    t3 = Entry(w, width=17, font=f, bd=5, show='*')
    t3.place(x=390, y=290)

    l5 = Label(w, text="Enter  Confirm Password ", font=f, bg="#F5FFFA", bd=3)
    l5.place(x=20, y=390)

    t4 = Entry(w, width=17, font=f, bd=5, show='*')
    t4.place(x=390, y=390)

    b2 = Button(w, text="Change Password", font=f, bg="#1E90FF", width=20, bd=3)
    b2.place(x=200, y=500)

    w.mainloop()