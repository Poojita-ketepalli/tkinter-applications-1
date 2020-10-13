import tkinter
from tkinter import *

root=Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#9DF3C4")

def calculate():
    height_value=float(height.get())
    weight_value=float(weight.get())
    bmi=weight_value/(height_value*height_value)
    BMI.set(bmi)
    if(bmi<18.5):
        Result_entry.config(fg="red")
        result.set("Thin")
    elif (bmi > 18.5 and bmi<=24.9):
        Result_entry.config(fg="green")
        result.set("Healthy")
    elif (bmi > 25 and bmi<=29.9):
        Result_entry.config(fg="red")
        result.set("Over weight")
    else:
        Result_entry.config(fg="red")
        result.set("Obessed")

Weight_label=Label(root,text="Weight(KG)",font=("serif",12,"bold"),bg="#9DF3C4")
Weight_label.pack()
weight=StringVar()
Weight_entry=Entry(root,textvariable=weight,font=("serif",12,"bold"),width=10,bd=4)
Weight_entry.pack()

Height_label=Label(root,text="Height(meter)",font=("serif",12,"bold"),bg="#9DF3C4")
Height_label.pack()
height=StringVar()
Height_entry=Entry(root,textvariable=height,font=("serif",12,"bold"),width=10,bd=4)
Height_entry.pack()

BMI_label=Label(root,text="BMI",font=("serif",12,"bold"),bg="#9DF3C4")
BMI_label.pack()
BMI=StringVar()
BMI_entry=Entry(root,textvariable=BMI,font=("serif",12,"bold"),width=15,bd=4)
BMI_entry.pack()
result=StringVar()
Result_entry=Entry(root,textvariable=result,font=("serif",12,"bold"),width=15,bd=4)
Result_entry.pack()

Space_label=Label(root,text=" ",font=("serif",12,"bold"),bg="#9DF3C4")
Space_label.pack()
Calc_button=Button(root,text="Calculate",relief=FLAT,font=("serif",12,"bold"),command=calculate,fg="white",bg="black")
Calc_button.pack()



root.mainloop()
