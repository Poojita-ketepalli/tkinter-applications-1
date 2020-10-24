import tkinter 
from tkinter import *

window=tkinter.Tk()
window.title("calculator")
window.geometry("375x320")
window.resizable(0,0)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
def btn_equal():
    global expression
    result=str(eval(expression)) #eval function evaluates the string expressio directly
    input_text.set(result)
expression = ""
input_text = StringVar()

#creating a frame for the input field
input_frame = Frame(window,width=312,height=50,bd=4)
input_frame.pack(side = TOP)

#creating a input field inside the frame
input_field = Entry(input_frame , font = ('arialbold',18),textvariable=input_text,bd=6)
input_field.grid(column=0,row=0)
input_field.pack(ipady=8) #ipady is internal padding to increase the height of the input field

btns_frame = Frame(window,width=312,height=272.5,bg="grey")
btns_frame.pack()


_1 = Button(btns_frame, text='1', fg='white', bg='black', bd=4, command=lambda: btn_click(1), height=2, width=7,relief=RAISED)
_1.grid(row=2, column=0)
_2 = Button(btns_frame, text='2', fg='white', bg='black', bd=4, command=lambda: btn_click(2), height=2, width=7,relief=RAISED)
_2.grid(row=2, column=1)
_3 = Button(btns_frame, text='3', fg='white', bg='black', bd=4, command=lambda: btn_click(3), height=2, width=7,relief=RAISED)
_3.grid(row=2, column=2)
_4 = Button(btns_frame, text='4', fg='white', bg='black', bd=4, command=lambda: btn_click(4), height=2, width=7,relief=RAISED)
_4.grid(row=3, column=0)
_5 = Button(btns_frame, text='5', fg='white', bg='black', bd=4, command=lambda: btn_click(5), height=2, width=7,relief=RAISED)
_5.grid(row=3, column=1)
_6 = Button(btns_frame, text='6', fg='white', bg='black', bd=4, command=lambda: btn_click(6), height=2, width=7,relief=RAISED)
_6.grid(row=3, column=2)
_7 = Button(btns_frame, text='7', fg='white', bg='black', bd=4, command=lambda: btn_click(7), height=2, width=7,relief=RAISED)
_7.grid(row=4, column=0)
_8 = Button(btns_frame, text='8', fg='white', bg='black', bd=4, command=lambda: btn_click(8), height=2, width=7,relief=RAISED)
_8.grid(row=4, column=1)
_9 = Button(btns_frame, text='9', fg='white', bg='black', bd=4, command=lambda: btn_click(9), height=2, width=7,relief=RAISED)
_9.grid(row=4, column=2)
_0 = Button(btns_frame, text='0', fg='white', bg='black', bd=4, command=lambda: btn_click(0), height=2, width=7,relief=RAISED)
_0.grid(row=5, column=0)
plus = Button(btns_frame, text='+', fg='white', bg='black', bd=4, command=lambda: btn_click('+'), height=2, width=7,relief=RAISED)
plus.grid(row=2, column=3)
minus = Button(btns_frame, text='-', fg='white', bg='black', bd=4, command=lambda: btn_click('-'), height=2, width=7,relief=RAISED)
minus.grid(row=3, column=3)
multiply = Button(btns_frame, text='*', fg='white', bg='black', bd=4, command=lambda:btn_click('*'), height=2, width=7,relief=RAISED)
multiply.grid(row=4, column=3)
divide = Button(btns_frame, text='/', fg='white', bg='black', bd=4, command=lambda:btn_click('/'), height=2, width=7,relief=RAISED)
divide.grid(row=5, column=3)
equal = Button(btns_frame, text='=', fg='white', bd=4, command=btn_equal, height=2, width=7,relief=RAISED,bg="red")
equal.grid(row=5, column=2)
clear = Button(btns_frame, text='Clear', fg='white', bg='black', bd=4, command=btn_clear, height=2, width=7,relief=RAISED)
clear.grid(row=5, column=1)




window.mainloop()

