from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import calendar
from tkinter import messagebox

root = tk.Tk()
root.geometry('400x300')
root.title('Calender')


def show():
    if(year.get()==""):
        messagebox.showinfo("required","Plese enter year")
    else:

        m = int(month.get())
        y = int(year.get())
        output = calendar.month(y,m)

        cal.insert('end',output)

def clear():
        cal.delete(1.0,'end')
        year1.set("")

def exit():
        root.destroy()





img = ImageTk.PhotoImage(Image.open(r"F:\working\practice2\calender1\calendar1.png"))
label = Label(image=img)
label.place(x=170,y=3)



m_label = Label(root,text="Month",font=('verdana','10','bold'))
m_label.place(x=70,y=80)

month = Spinbox(root, from_= 1, to = 12,width="5") 
month.place(x=140,y=80) 
  
y_label = Label(root,text="Year",font=('verdana','10','bold'))
y_label.place(x=210,y=80)

year1=StringVar()
year = Entry(root,width="8",textvariable=year1) 
year.place(x=260,y=80) 


cal = Text(root,width=33,height=8,relief=RIDGE,borderwidth=2)
cal.place(x=70,y=110)

show = Button(root,text="Show",font=('italic',10,'bold'),relief=FLAT,command=show)
show.place(x=140,y=250)

clear = Button(root,text="Clear",font=('italic',10,'bold'),relief=FLAT,command=clear)
clear.place(x=200,y=250)

exit = Button(root,text="Exit",font=('italic',10,'bold'),relief=FLAT,command=exit)
exit.place(x=260,y=250)
root.mainloop()