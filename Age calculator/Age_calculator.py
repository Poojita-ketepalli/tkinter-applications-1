from tkinter import *
from datetime import date
from tkinter import messagebox

root=Tk()
root.title("AGE CALCULATOR")
root.geometry("900x600")
root.config(bg="#71F4EB")

def check():
    if(entry1.get()=="" or entry2.get()=="" or entry3.get()==""):
        messagebox.showerror("Error","Please fill all the columns")

    else:
        # take a value from the respective entry boxes 
        # get method returns current text as string 
        birth_day = int(entry1.get()) 
        birth_month = int(entry2.get()) 
        birth_year = int(entry3.get()) 
  
        given_day = int(entry4.get()) 
        given_month = int(entry5.get()) 
        given_year = int(entry6.get())
            
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
          
        if (birth_day > given_day): 
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]  
                        
        if (birth_month > given_month): 
            given_year = given_year - 1
            given_month = given_month + 12
                        
        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        result=str(calculated_year)+"years,"+str(calculated_month)+"months,"+str(calculated_day)+"days"
        entry7.set(result)
  

lbl_day=Label(root,text="Birth Day",bg="#71F4EB",font=("Comic Sans MS",15,"bold"))
lbl_day.grid(row=2,column=0,sticky=W)
lbl_month=Label(root,text="Birth Month",bg="#71F4EB",font=("Comic Sans MS",15,"bold"))
lbl_month.grid(row=3,column=0,sticky=W)
lbl_year=Label(root,text="Birth Year",bg="#71F4EB",font=("Comic Sans MS",15,"bold"))
lbl_year.grid(row=4,column=0,sticky=W)

entry1=StringVar()
entry2=StringVar()
entry3=StringVar()
entry4=StringVar()
entry5=StringVar()
entry6=StringVar()
entry7=StringVar()

entry_day=Entry(root,font=("Comic Sans MS",8,"bold"),bd=3,textvariable=entry1)
entry_day.grid(row=2,column=1)
entry_month=Entry(root,font=("Comic Sans MS",8,"bold"),bd=3,textvariable=entry2)
entry_month.grid(row=3,column=1)
entry_year=Entry(root,font=("Comic Sans MS",8,"bold"),bd=3,textvariable=entry3)
entry_year.grid(row=4,column=1)

lbl_day1=Label(root,text="Present Day",bg="#71F4EB",font=("Comic Sans MS",15,"bold"))
lbl_day1.grid(row=2,column=3,sticky=W)
lbl_month1=Label(root,text="Present Month",bg="#71F4EB",font=("Comic Sans MS",15,"bold"))
lbl_month1.grid(row=3,column=3,sticky=W)
lbl_year1=Label(root,text="Present Year",bg="#71F4EB",font=("Comic Sans MS",15,"bold"))
lbl_year1.grid(row=4,column=3,sticky=W)

entry_day1=Entry(root,font=("Comic Sans MS",8,"bold"),bd=3,textvariable=entry4)
entry_day1.grid(row=2,column=4)
entry_month1=Entry(root,font=("Comic Sans MS",8,"bold"),bd=3,textvariable=entry5)
entry_month1.grid(row=3,column=4)
entry_year1=Entry(root,font=("Comic Sans MS",8,"bold"),bd=3,textvariable=entry6)
entry_year1.grid(row=4,column=4)

lbl_space=Label(root,text="",bg="#71F4EB")
lbl_space.grid(row=5,column=2)

button_check=Button(root,text="CHECK",font=("Comic Sans MS",12,"bold"),bg="#F71010",fg="white",command=check)
button_check.grid(row=6,column=2)

current_date=date.today()
entry4.set(current_date.day)
entry6.set(current_date.year)
entry5.set(current_date.month)

lbl_space=Label(root,text="",bg="#71F4EB")
lbl_space.grid(row=7,column=2)

lbl_age=Label(root,text="Your Age",bg="#71F4EB",font=("Comic Sans MS",15,"bold"))
lbl_age.grid(row=8,column=2)
entry_age=Entry(root,font=("Comic Sans MS",10,"bold"),bd=3,textvariable=entry7)
entry_age.grid(row=9,column=2)


root.mainloop()