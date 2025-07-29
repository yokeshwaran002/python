from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Radiobutton")
root.geometry("500x400")

var=IntVar()

r1=Checkbutton(root,variable=var,text="Male")
r1.pack()

var1=IntVar()

r2=Checkbutton(root,variable=var1,text="Female")
r2.pack()


def submit():
    a=var.get(),var1.get()
    print(a)
    



b=Button(root,text="Submit",command=submit)
b.pack()

mainloop()