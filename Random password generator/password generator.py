from tkinter import *
import random,string

root=Tk()
root.title("Random Password generator")
root.geometry("400x400")
root.config(background="#04f4f5")

length=StringVar()
length_label=Label(root,text="Length of the password",bg="#04f4f5",font=("serif",12,"bold"))
length_label.place(x=70,y=10)
length_entry=Entry(root,font=("serif",12,"bold"),textvariable=length)
length_entry.place(x=70,y=50)

password=StringVar()
password_label=Label(root,text="Password",bg="#04f4f5",font=("serif",12,"bold"))
password_label.place(x=130,y=160)
password_entry=Entry(root,font=("serif",12,"bold"),textvariable=password)
password_entry.place(x=70,y=200)

strength=StringVar()
strength_label=Label(root,text="Password Strength",bg="#04f4f5",font=("serif",12,"bold"))
strength_label.place(x=80,y=240)
strength_entry=Entry(root,font=("serif",12,"bold"),textvariable=strength)
strength_entry.place(x=70,y=280)

def generate():
    l=int(length.get())
    if l<=6:
        strength.set("Weak")
        strength_entry.config(fg="red")
    elif l<=10 and l>6:
        strength.set("Medium")
        strength_entry.config(fg="blue")
    elif l<=15 and l>10:
        strength.set("Strong")
        strength_entry.config(fg="#678348")
    else:
        strength.set("Very Strong")
        strength_entry.config(fg="#f607e3")
    letters='!@#$%^&*()'+string.ascii_letters+string.digits
    password1=''
    for i in range(l):
        password1=password1+str((''.join(random.choice(letters,))))
        password.set(password1)

def clear():
    password.set(" ")
    strength.set(" ")
    length.set("")

generate_button=Button(root,text="Generate",font=("serif",12,"bold"),bg="#fb05f1",command=generate,width=10)
generate_button.place(x=50,y=100)
clear_button=Button(root,text="Clear",font=("serif",12,"bold"),bg="#fb05f1",command=clear,width=10)
clear_button.place(x=230,y=100)


root.mainloop()