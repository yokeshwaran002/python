
from tkinter import *
root=Tk()
root.title("task")
root.geometry("500x400")

name= Label(root, text="Name")
name.pack()
t1 = Entry(root,background="lightpink")
t1.pack()

age=Label(root, text="Age")
age.pack()
t2 = Entry(root,background="lightpink")
t2.pack()

s=Label(root, text="Output")
s.pack()
t3 = Entry(root)
t3.pack()

def submit():
    a = (t1.get(), t2.get())
    t3.delete(0, END)
    t3.insert(0, a)
    print(a)

button = Button(root, text="Submit", command=submit,background="red")
button.pack()

mainloop()

