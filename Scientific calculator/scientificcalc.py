from tkinter import *
import math
from tkinter import messagebox
from fractions import Fraction

window=Tk()
window.title("calculator")
window.geometry("620x550+400+200")
window.configure(bg="gray")
window.resizable(0,0)

def btn_click(item):
    global expression
    try:
        result = expression + str(item)
        input_text.set(result)
        expression=result
    except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
def btn_equal():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=str(eval(expression)) #eval function evaluates the string expressio directly
            input_text.set(result)
            expression=result
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")

def cos():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.cos(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}") 
def sin():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.sin(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def tan():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.tan(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def cosh():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.cosh(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def sinh():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.sinh(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def tanh():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.tanh(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def invsin():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.asin(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def invcos():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.acos(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def invtan():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.atan(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def exp():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.exp(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def lan():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.log(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def square():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=(int(expression)**2)
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def cubic():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=(int(expression)**3)
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def delete():
    global expression
    i = input_text.get()
    if len(i)==0:
        input_text.set("")
        expression=""
    else:
        newtext=i[:-1]
        input_text.set("")
        input_text.set(newtext)
        expression=newtext
def power10():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=10**int(expression)
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def binfun():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=(bin(int(expression)))
            result1=result[2:]
            input_text.set(result1)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def squareroot():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.sqrt(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def divfrac():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=str(Fraction(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")

expression = ""

input_frame = Frame(window,width=500,height=100,relief=RAISED,bg="gray")
input_frame.pack(side = TOP)

input_text=StringVar()
input_field = Entry(input_frame,font = ('arialbold',15),textvariable=input_text,border=8,width=420,bg="gray70")
input_field.grid(column=0,row=0)
input_field.pack(ipady=10,padx=30)

btns_frame = Frame(window,width=500,height=340,bg="grey")
btns_frame.pack()

_1 = Button(btns_frame, text='1', fg='white', bg='black', bd=3, command=lambda: btn_click(1), height=4, width=7,relief=RAISED)
_1.grid(row=2, column=0)
_2 = Button(btns_frame, text='2', fg='white', bg='black', bd=3, command=lambda: btn_click(2), height=4, width=7,relief=RAISED)
_2.grid(row=2, column=1)
_3 = Button(btns_frame, text='3', fg='white', bg='black', bd=3, command=lambda: btn_click(3), height=4, width=7,relief=RAISED)
_3.grid(row=2, column=2)
_4 = Button(btns_frame, text='4', fg='white', bg='black', bd=3, command=lambda: btn_click(4), height=4, width=7,relief=RAISED)
_4.grid(row=3, column=0)
_5 = Button(btns_frame, text='5', fg='white', bg='black', bd=3, command=lambda: btn_click(5), height=4, width=7,relief=RAISED)
_5.grid(row=3, column=1)
_6 = Button(btns_frame, text='6', fg='white', bg='black', bd=3, command=lambda: btn_click(6), height=4, width=7,relief=RAISED)
_6.grid(row=3, column=2)
_7 = Button(btns_frame, text='7', fg='white', bg='black', bd=3, command=lambda: btn_click(7), height=4, width=7,relief=RAISED)
_7.grid(row=4, column=0)
_8 = Button(btns_frame, text='8', fg='white', bg='black', bd=3, command=lambda: btn_click(8), height=4, width=7,relief=RAISED)
_8.grid(row=4, column=1)
_9 = Button(btns_frame, text='9', fg='white', bg='black', bd=3, command=lambda: btn_click(9), height=4, width=7,relief=RAISED)
_9.grid(row=4, column=2)
_0 = Button(btns_frame, text='0', fg='white', bg='black', bd=3, command=lambda: btn_click(0), height=4, width=7,relief=RAISED)
_0.grid(row=5, column=0)
plus = Button(btns_frame, text='+', fg='white', bg='black', bd=3, command=lambda: btn_click('+'), height=4, width=7,relief=RAISED)
plus.grid(row=2, column=3)
minus = Button(btns_frame, text='-', fg='white', bg='black', bd=3, command=lambda: btn_click('-'), height=4, width=7,relief=RAISED)
minus.grid(row=3, column=3)
multiply = Button(btns_frame, text='*', fg='white', bg='black', bd=3, command=lambda:btn_click('*'), height=4, width=7,relief=RAISED)
multiply.grid(row=4, column=3)
divide = Button(btns_frame, text='/', fg='white', bg='black', bd=3, command=lambda:btn_click('/'), height=4, width=7,relief=RAISED)
divide.grid(row=5, column=3)
equal = Button(btns_frame, text='=', fg='white', bg='red', bd=3, command=btn_equal, height=4, width=7,relief=RAISED)
equal.grid(row=5, column=2)
clear = Button(btns_frame, text='Clear', fg='white', bg='black', bd=3, command=btn_clear, height=4, width=7,relief=RAISED)
clear.grid(row=5, column=1)

lblcos = Button(btns_frame, text='cos', fg='white', bg='gray', bd=3, command=cos, height=4, width=7,relief=RAISED)
lblcos.grid(row=2, column=4)
lblsin = Button(btns_frame, text='sin', fg='white', bg='gray', bd=3, command=sin, height=4, width=7,relief=RAISED)
lblsin.grid(row=2, column=5)
lbltan = Button(btns_frame, text='tan', fg='white',bg='gray', bd=3, command=tan, height=4, width=7,relief=RAISED)
lbltan.grid(row=2, column=6)
lblsinh = Button(btns_frame, text='sinh', fg='white',bg='gray', bd=3, command=sinh, height=4, width=7,relief=RAISED)
lblsinh.grid(row=3, column=4)
lblcosh = Button(btns_frame, text='cosh', fg='white', bg='gray', bd=3, command=cosh, height=4, width=7,relief=RAISED)
lblcosh.grid(row=3, column=5)
lbltanh = Button(btns_frame, text='tanh', fg='white', bg='gray', bd=3, command=tanh, height=4, width=7,relief=RAISED)
lbltanh.grid(row=3, column=6)
lblinvsin = Button(btns_frame, text='inv(sin)', fg='white', bg='gray', bd=3, command=invsin, height=4, width=7,relief=RAISED)
lblinvsin.grid(row=4, column=4)
lblinvcos = Button(btns_frame, text='inv(cos)', fg='white', bg='gray', bd=3, command=invcos, height=4, width=7,relief=RAISED)
lblinvcos.grid(row=4, column=5)
lblinvtan = Button(btns_frame, text='inv(tan)', fg='white',bg='gray', bd=3, command=invtan, height=4, width=7,relief=RAISED)
lblinvtan.grid(row=4, column=6)
point = Button(btns_frame, text='.', fg='white', bg='black', bd=3, command=lambda: btn_click("."), height=4, width=7,relief=RAISED)
point.grid(row=5, column=4)
expo = Button(btns_frame, text='e', fg='white', bg='black', bd=3, command=exp, height=4, width=7,relief=RAISED)
expo.grid(row=2, column=7)
sqr = Button(btns_frame, text=' x²', fg='white', bg='black', bd=3, command=square, height=4, width=7,relief=RAISED)
sqr.grid(row=3, column=7)
cube = Button(btns_frame, text='x³', fg='white', bg='black', bd=3, command=cubic, height=4, width=7,relief=RAISED)
cube.grid(row=4, column=7)
pi = Button(btns_frame, text='π', fg='white', bg='black', bd=3, command=lambda:btn_click(3.14), height=4, width=7,relief=RAISED)
pi.grid(row=5, column=7)
pi2 = Button(btns_frame, text='2π', fg='white', bg='black', bd=3, command=lambda:btn_click(6.28), height=4, width=7,relief=RAISED)
pi2.grid(row=5, column=6)
lbllog = Button(btns_frame, text='10^x', fg='white', bg='black', bd=3, command=power10, height=4, width=7,relief=RAISED)
lbllog.grid(row=5, column=5)

percent = Button(btns_frame, text='floor', fg='white', bg='black', bd=3,command=lambda:btn_click('//'), height=4, width=7,relief=RAISED)
percent.grid(row=1, column=0)
lbldel= Button(btns_frame, text='del', fg='white', bg='black', bd=3, command=delete, height=4, width=7,relief=RAISED)
lbldel.grid(row=1, column=1)
mod = Button(btns_frame, text='MOD', fg='white', bg='black', bd=3, command=lambda:btn_click('%'), height=4, width=7,relief=RAISED)
mod.grid(row=1, column=2)
lan = Button(btns_frame, text='ln', fg='white', bg='black', bd=3, command=lan, height=4, width=7,relief=RAISED)
lan.grid(row=1, column=3)
power = Button(btns_frame, text='pow', fg='white', bg='black', bd=3, command=lambda:btn_click('**'), height=4, width=7,relief=RAISED)
power.grid(row=1, column=4)
binary = Button(btns_frame, text='bin', fg='white', bg='black', bd=3, command=binfun, height=4, width=7,relief=RAISED)
binary.grid(row=1, column=5)
frac = Button(btns_frame, text='D-F', fg='white', bg='black', bd=3,command=divfrac, height=4, width=7,relief=RAISED)
frac.grid(row=1, column=6)
sqrt = Button(btns_frame, text='√ ', fg='white', bg='black', bd=3, command=squareroot, height=4, width=7,relief=RAISED)
sqrt.grid(row=1, column=7)

def log10():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.log10(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def log2():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.log2(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def absolute():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=abs(float(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def fact():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=math.factorial(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")
def onediv():
    global expression
    if expression=="":
        messagebox.showerror("Error","Enter some value to calculate",parent=window)
    else:
        try:
            result=1/(int(expression))
            input_text.set(result)
            expression=str(result)
        except Exception as es:
            messagebox.showerror("Error",f"the error is {str(es)}")

sqrt = Button(btns_frame, text='| x | ', fg='white', bg='black', bd=3, command=absolute, height=4, width=7,relief=RAISED)
sqrt.grid(row=1, column=8)
sqrt = Button(btns_frame, text='x ! ', fg='white', bg='black', bd=3, command=fact, height=4, width=7,relief=RAISED)
sqrt.grid(row=2, column=8)
sqrt = Button(btns_frame, text='1/ x ', fg='white', bg='black', bd=3, command=onediv, height=4, width=7,relief=RAISED)
sqrt.grid(row=3, column=8)
sqrt = Button(btns_frame, text='log10 ', fg='white', bg='black', bd=3, command=log10, height=4, width=7,relief=RAISED)
sqrt.grid(row=4, column=8)
sqrt = Button(btns_frame, text='log2 ', fg='white', bg='black', bd=3, command=log2, height=4, width=7,relief=RAISED)
sqrt.grid(row=5, column=8)






window.mainloop()
