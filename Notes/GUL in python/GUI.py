'''from tkinter import *
r = Tk()
r.geometry("400x100")
name = Label(r, text="S.yokeshwaran")
name.pack()
age = Label(r, text="18")
age.pack()
collage = Label(r, text="AVC Collage")
collage.pack()
r.mainloop()'''


'''from tkinter import *

root=Tk()
root.title("Frame")
root.geometry("500x400")

f = Label(root, text="blue")
f.pack()
f=Frame(root,width=1000,height=50,background="blue")
f.pack()

b= Label(root, text="black")
b.pack()
b=Frame(root,width=1000,height=50,background="black")
b.pack()

p= Label(root, text="pink")
p.pack()
p=Frame(root,width=1000,height=50,background="pink")
p.pack()

g = Label(root, text="green")
g.pack()
g=Frame(root,width=1000,height=50,background="green")
g.pack()

r = Label(root, text="red")
r.pack()
r=Frame(root,width=1000,height=50,background="red")
r.pack()

u = Label(root, text="purple")
u.pack()
u=Frame(root,width=1000,height=50,background="purple")
u.pack()

y = Label(root, text="yellow")
y.pack()
y=Frame(root,width=1000,height=50,background="yellow")
y.pack()

o = Label(root, text="brown")
o.pack()
o=Frame(root,width=1000,height=50,background="brown")
o.pack()

w = Label(root, text="white")
w.pack()
w=Frame(root,width=1000,height=50,background="white")
w.pack()

o = Label(root, text="orange")
o.pack()
o=Frame(root,width=1000,height=50,background="orange")
o.pack()

root.mainloop()'''

'''from tkinter import *

root=Tk()
root.title("Frame")
root.geometry("500x400")

f=Frame(root,width=100,height=50,background="blue")
f.grid(row=0, column=0)

f=Frame(root,width=100,height=50,background="orange")
f.grid(row=1, column=1)

f=Frame(root,width=100,height=50,background="brown")
f.grid(row=2, column=2)

f=Frame(root,width=100,height=50,background="green")
f.grid(row=3, column=3)

f=Frame(root,width=100,height=50,background="pink")
f.grid(row=5, column=5)

root.mainloop()'''

'''from tkinter import *

root=Tk()
root.title("Frame")
root.geometry("500x400")

from tkinter import *

root=Tk()
root.title("Frame")
root.geometry("500x400")

f1 = Label(root, text="red")
f1.grid(row=1,column=0)
f1=Frame(root,width=100,height=50,background="red")
f1.grid(row=1,column=1)

f2= Label(root, text="pink")
f2.grid(row=2,column=0)
f2=Frame(root,width=100,height=50,background="pink")
f2.grid(row=2,column=1)

f3 = Label(root, text="green")
f3.grid(row=3,column=0)
f3=Frame(root,width=100,height=50,background="green")
f3.grid(row=3,column=1)

f4 = Label(root, text="black")
f4.grid(row=4,column=0)
f4=Frame(root,width=100,height=50,background="black")
f4.grid(row=4,column=1)
root.mainloop()

from tkinter import *
root=Tk()
root.title("for loop")
root.geometry("500x400")

x = ["red", "pink", "green", "black","lightpink", "lightgreen","brown","orange","blue","purple","yellow"]
for color in x:
	f = Frame(root, width=100, height=50, background=color)
	f.place(x=0,y=10)	
root.mainloop()'''

'''from tkinter import *
r = Tk()
r.geometry("400x100")
r.title("place")

n = Label(r, text="S.yokeshwaran")
n.place(x=77, y=130)
b = Frame(r, width=100, height=50, background="red")
b.place(x=169,y=10)

r.mainloop()'''

'''from tkinter import *
root=Tk()
root.title("Button")
root.geometry("500x400")

e1=Entry(root)
e1.pack()

e2=Entry(root)
e2.pack()

e3=Entry(root)
e3.pack()

def submit():
    a=int(e1.get())+int(e2.get())
    e3.delete(0,END)
    e3.insert(0,a)

button = Button(root,text="Submit",command=submit)
button.pack()
mainloop()'''



#combo box

'''from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("300x200")


l = ttk.Label(root, text="Select option")
l.place(x=10, y=10)


options = ["select", "tamilnadu", "kerala", "karnataka", "andhra"]


combobox = ttk.Combobox(root, values=options, state="readonly")
combobox.place(x=120, y=10)
combobox.set(options[0])


def submit():
    selected = combobox.get()
    if selected == "tamilnadu":
        print("tamilnadu")
    elif selected == "kerala":
        print("kerala")
    elif selected == "karnataka":
        print("karnataka")
    elif selected == "andhra":
        print("andhra")
    else:
        messagebox.showinfo("Error", "Please select a valid option")

button = Button(root, text="Submit", command=submit)
button.place(x=120, y=50)

root.mainloop()'''



'''
#adding image

from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Image")

bimage=Image.open("backdrop.png")
bphoto=ImageTk.PhotoImage(bimage.resize((500,400)))


l=Label(root,image=bphoto)
l.place(x=10,y=10,relwidth=1,relheight=1)

root.mainloop()'''

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def submit_action():
    user_name = t1.get()
    user_age = t2.get()
    if not user_name or not user_age:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
    else:
        messagebox.showinfo("Submitted", f"Name: {user_name}\nAge: {user_age}")

root = Tk()
root.title("Image")
root.geometry("800x500")

#background
br_image = Image.open("backdrop.png")
br_photo = ImageTk.PhotoImage(br_image.resize((800, 500)))

l = Label(root, image=br_photo)
l.place(x=0, y=0, relwidth=1, relheight=1)

#Name 
name = Label(root, text="Name", bg="white")
name.place(x=500, y=150)
t1 = Entry(root)
t1.place(x=550, y=151)

#Age 
age = Label(root, text="Age", bg="white")
age.place(x=500, y=200)
t2 = Entry(root)
t2.place(x=550, y=201)

#button
buoton_var = IntVar()
buoton_cb = Checkbutton(root, text="i not robot", variable=buoton_var, bg="white")
buoton_cb.place(x=550, y=230)

button = Button(root, text="Submit", command=submit_action)
button.place(x=550, y=300)

root.mainloop()
