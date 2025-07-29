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
root.mainloop()'''

'''from tkinter import *
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

from tkinter import *
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
mainloop()

