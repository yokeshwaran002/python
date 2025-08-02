


# tas

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("login page form ")
root.geometry("500x400")

name= Label(root, text="Name")
name.grid(row=0,column=0)
t1 = Entry(root)
t1.grid(row=0,column=1)

age=Label(root, text="Age")
age.grid(row=1,column=0)
t2 = Entry(root)
t2.grid(row=1,column=1)

agree_var = IntVar()
agree_cb = Checkbutton(root, text="i not robot", variable=agree_var, bg="white")
agree_cb.place(x=500, y=230)

var=IntVar()
gender= Label(root, text="gender:-")
gender.grid(row=2,column=0)
r1=Radiobutton(root,variable=var,value=1,text="Male")
r1.grid(row=5,column=1)

r2=Radiobutton(root,variable=var,value=2,text="Female")
r2.grid(row=6,column=1)
def submit():
    a = (t1.get(), t2.get(), var1.get())
    if var1.get() == 1:
        print(a)
var1=IntVar()
course= Label(root, text="course:-")
course.grid(row=7,column=0)

r1=Checkbutton(root,variable=var1,text="python course")
r1.grid(row=8,column=1)

var2=IntVar()

r2=Checkbutton(root,variable=var2,text="java course")
r2.grid(row=9,column=1)

var3=IntVar()

r3=Checkbutton(root,variable=var3,text="c++ course")
r3.grid(row=10,column=1)

var4=IntVar()
r4=Checkbutton(root,variable=var4,text="c# course")
r4.grid(row=11,column=1)
def submit():
    a = t1.get(), t2.get()
    b= var.get()
    c= var1.get(),var2.get(), var3.get(), var4.get()
    print(a)
    if b == 1:
        print("Male")
    elif b== 2:
        print("Female")
    else:
        messagebox.showinfo("Error", "Please select option")
    print(c)

b=Button(root,text="Submit",command=submit)
b.grid(row=12,column=1)


mainloop()