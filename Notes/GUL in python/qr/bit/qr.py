from tkinter import *
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    data = entry.get()
    qr_img = qrcode.make(data)
    qr_img = qr_img.resize((200, 200))
    img = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=img)
    qr_label.image = img

root = Tk()
root.title("QR Code Generator")
root.geometry("300x350")

Label(root, text="Enter text or URL:").pack(pady=10)
entry = Entry(root, width=30)
entry.pack(pady=5)

Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = Label(root)
qr_label.pack(pady=20)

root.mainloop()