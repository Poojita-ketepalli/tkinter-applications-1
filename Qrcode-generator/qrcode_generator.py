#pip install pyqrcode

import pyqrcode
from tkinter import *
#import tkinter.ttk as ttk
from PIL import Image,ImageTk

win=Tk()
win.title("QR Code Generator")
win.config(background="#FF5733")

def generate():
    text=entry1.get()
    qr=pyqrcode.create(text)
    file_name=filename.get()
    save_path=r"E:\working\practice1\Qrcode-generator"
    name=save_path+file_name+'.png'

    qr.png(name,scale=10)
    image=Image.open(name)
    image=image.resize((400,400),Image.ANTIALIAS)
    image=ImageTk.PhotoImage(image)
    win.imagelabel.config(image=image)
    win.imagelabel.photo=image

def reset():
    filename.set("")
    entry.set("")

filename_label=Label(win,text="Enter Filename:",font=("serif",12,"bold"),bg="#FF5733")
filename_label.grid(row=1,column=0,padx=3,pady=3)

filename=StringVar()
entry2=Entry(win,width=40,textvariable=filename)
entry2.grid(row=1,column=1,padx=3,pady=3)

text=Label(win,text="Enter text or Link :",font=("serif",12,"bold"),bg="#FF5733")
text.grid(row=2,column=0,padx=3,pady=3)

entry=StringVar()
entry1=Entry(win,width=40,textvariable=entry)
entry1.grid(row=2,column=1,padx=3,pady=3)

button=Button(win,text="Generate",command=generate,font=("serif",12,"bold"),bg="#FF5733")
button.grid(row=1,column=2,padx=3,pady=3)

button1=Button(win,text="Reset",command=reset,font=("serif",12,"bold"),bg="#FF5733")
button1.grid(row=2,column=2,padx=3,pady=3)

show_qr=Label(win,text="Qr Code:",font=("serif",15,"bold"),bg="#FF5733",fg="white")
show_qr.grid(row=3,column=0,padx=3,pady=3)

win.imagelabel=Label(win,background="#FF5733")
win.imagelabel.grid(row=3,column=0,padx=3,pady=3,columnspan=3)


win.mainloop()

    