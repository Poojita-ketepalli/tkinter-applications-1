from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("600x330+300+100")
root.title("TIC-TAC-TOE")
root.resizable(False,False)
frame1=Frame(root,height=300,width=600,bg="#FF6464",relief=SUNKEN,bd=10)
frame1.pack()
frame2=Frame(frame1,height=100,width=590,bg="#FF6464",relief=RAISED,bd=3)
frame2.pack(side=TOP)
frame3=Frame(frame1,height=230,width=590,bg="#FF6464",relief=FLAT,bd=3)
frame3.pack(side=TOP)

heading=Label(frame2,text="TIC-TAC-TOE",font=("Times new roman",30,"bold"),bg="#FF6464",width=580)
heading.pack()

button1=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button1))
button1.grid(row=1,column=0)
button2=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button2))
button2.grid(row=1,column=1)
button3=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button3))
button3.grid(row=1,column=2)
button4=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button4))
button4.grid(row=2,column=0)
button5=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button5))
button5.grid(row=2,column=1)
button6=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button6))
button6.grid(row=2,column=2)
button7=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button7))
button7.grid(row=3,column=0)
button8=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button8))
button8.grid(row=3,column=1)
button9=Button(frame3,text=" ",width=10,height=3,state=DISABLED,bg="grey89",relief=RAISED,bd=4,command=lambda:btnclick(button9))
button9.grid(row=3,column=2)

label_space1=Label(frame3,text="\t",width=8,height=1,font=("serif",10,"bold"),bg="#FF6464")
label_space1.grid(row=1,column=3)
label_space2=Label(frame3,text="\t",width=8,height=1,font=("serif",10,"bold"),bg="#FF6464")
label_space2.grid(row=2,column=3)
label_space3=Label(frame3,text="\t",width=8,height=1,font=("serif",10,"bold"),bg="#FF6464")
label_space3.grid(row=3,column=3)

def reset():
    global count
    count=1
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button1.config(bg="grey89")
    button2.config(bg="grey89")
    button3.config(bg="grey89")
    button4.config(bg="grey89")
    button5.config(bg="grey89")
    button6.config(bg="grey89")
    button7.config(bg="grey89")
    button8.config(bg="grey89")
    button9.config(bg="grey89")
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
def start():
    global count
    count=0
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=NORMAL)
    button6.config(state=NORMAL)
    button7.config(state=NORMAL)
    button8.config(state=NORMAL)
    button9.config(state=NORMAL)
    button1.config(bg="grey30")
    button2.config(bg="grey30")
    button3.config(bg="grey30")
    button4.config(bg="grey30")
    button5.config(bg="grey30")
    button6.config(bg="grey30")
    button7.config(bg="grey30")
    button8.config(bg="grey30")
    button9.config(bg="grey30")
count=0
def btnclick(button):
    global count
    if(count%2==0):
        button["text"]="O"
        button.config(state=DISABLED)
        button.config(bg="grey89")
        count+=1
        win()
    else:
        button["text"]="x"
        button.config(state=DISABLED)
        button.config(bg="grey89")
        count+=1
        win()

def win():
    if((button1["text"]=="x" and button2["text"]=="x" and button3["text"]=="x") or
        (button4["text"]=="x" and button5["text"]=="x" and button6["text"]=="x") or
        (button7["text"]=="x" and button8["text"]=="x" and button9["text"]=="x") or
        (button1["text"]=="x" and button4["text"]=="x" and button7["text"]=="x") or
        (button2["text"]=="x" and button5["text"]=="x" and button8["text"]=="x") or
        (button9["text"]=="x" and button6["text"]=="x" and button3["text"]=="x") or
        (button1["text"]=="x" and button5["text"]=="x" and button9["text"]=="x") or
        (button3["text"]=="x" and button5["text"]=="x" and button7["text"]=="x")):
        messagebox.showinfo("WINNER","PLAYER 1 WINS")
    elif((button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O") or
        (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O") or
        (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O") or
        (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O") or
        (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O") or
        (button9["text"]=="O" and button6["text"]=="O" and button3["text"]=="O") or
        (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O") or
        (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O")):
        messagebox.showinfo("WINNER","PLAYER 2 WINS")
    elif(count%9==0):
        messagebox.showinfo("WINNER","DRAW MATCH")




button_start=Button(frame3,text="START",width=8,height=1,font=("serif",10,"bold"),command=start)
button_start.grid(row=1,column=4)
button_reset=Button(frame3,text="RESET",width=8,height=1,font=("serif",10,"bold"),command=reset)
button_reset.grid(row=2,column=4)
button_exit=Button(frame3,text="EXIT",width=8,height=1,font=("serif",10,"bold"),command=exit)
button_exit.grid(row=3,column=4)

root.mainloop()