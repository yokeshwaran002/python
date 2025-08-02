from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Radiobutton")
root.geometry("500x400")

var=IntVar()

r1=Radiobutton(root,variable=var,value=1,text="Male")
r1.pack()

r2=Radiobutton(root,variable=var,value=2,text="Female")
r2.pack()


def submit():
    a=var.get()
    if a==1:
        print("Male")
    elif a==2:
        print("Female")
    else:
        messagebox.showinfo("Error","Please select option")



b=Button(root,text="Submit",command=submit)
b.pack()

mainloop()