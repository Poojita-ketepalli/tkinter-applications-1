from tkinter import *
import webbrowser

root=Tk()
root.title("Web browser")
root.geometry("400x400+100+100")
root.config(bg="white")

button1=Button(root,text="Youtube",font=("serif",15,"bold"),bg="red",fg="white")
button1.place(x=40,y=100)


root.mainloop()