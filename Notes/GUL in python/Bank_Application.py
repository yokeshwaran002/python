import tkinter as tk
from tkinter import messagebox

USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = u2.get()
    pas  = p2.get()
    
    if user == USERNAME and pas == PASSWORD:
        messagebox.showinfo("Login Success")
    else:
        messagebox.showerror("Login Failed")

root = tk.Tk()
root.title("Bank Application Login")
root.geometry("350x250")

title = tk.Label(root, text="Bank Login" ,font=(15))
title.pack(pady=10)

u1 = tk.Label(root, text="Username")
u1.pack(pady=(10, 0))
u2 = tk.Entry(root, width=30)
u2.pack(pady=5)

p1 = tk.Label(root, text="Password:")
p1.pack(pady=(10, 0))
p2 = tk.Entry(root, width=30,show="*")
p2.pack(pady=5)

button = tk.Button(root, text="Login", command=login, width=20)
button.pack(pady=20)

root.mainloop()
