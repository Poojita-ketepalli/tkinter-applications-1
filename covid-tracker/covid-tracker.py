import covid
from tkinter import *
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tkinter import messagebox

root=Tk()
root.title("Covis-19 status App")

def show_countries():
    screen=Toplevel()
    screen.title("Countries List")
    screen.geometry("800x500+100+100")
    scrollbar=Scrollbar(screen,orient=VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    text=Text(screen,yscrollcommand=scrollbar.set)
    text.pack(fill=BOTH,expand=YES)
    
    data=covid.Covid()
    country_name=e1.get()
    text.insert(END,data.list_countries())
        
        

def show_data():
    try:
        data=covid.Covid()
        country_name=e1.get()
        #x=data.list_countries()
        status=data.get_status_by_country_name(country_name)
        active=status['active']
        e2.insert(0,active)
        death=status['deaths']
        e3.insert(0,death)
        confirmed=status['confirmed']
        e4.insert(0,confirmed)
        recovered=status['recovered']
        e5.insert(0,recovered)

        data={'id':str(status['id']),
              'Country':str(status['country']),
              'Confirmed':str(status['confirmed']),
              'Active':str(status['active']),
              'Deaths':str(status['deaths']),
              'Recovered':str(status['recovered']),
              'Latitude':str(status['latitude']),
              'Longitude':str(status['longitude']),
              'Last_updated':str(status['last_update']),
        }
        df=pd.DataFrame(data,index=[0])
        print(df)
        cadr={key:status[key]
              for key in {'confirmed','active','deaths','recovered'}
        }
        n=list(cadr.keys())
        v=list(cadr.values())
        plt.title("Country")
        plt.bar(range(len(cadr)),v,tick_label=n,label=('active'))
        plt.xlabel('x-labels')
        plt.ylabel('data')
        plt.plot(range(len(cadr)))
        y=plt.show()
    except Exception as es:
        messagebox.showerror("Error",f"Error due to {str(es)}")
def clear():
    e11.set("")
    e21.set("")
    e31.set("")
    e41.set("")
    e51.set("")
def exit():
    root.destroy()
    
e11=StringVar()
e21=StringVar()
e31=StringVar()
e41=StringVar()
e51=StringVar()

Label(root,text="Enter country name",font=("Serif",10,"bold")).grid(row=2,column=2)
e1=Entry(root,bd=3,textvariable=e11)
e1.grid(row=2,column=3)

Label(root,text="",font=("Serif",6,"bold")).grid(row=6,column=2)
Label(root,text="Active cases",font=("Serif",10,"bold")).grid(row=8,column=2)
Label(root,text="",font=("Serif",10,"bold")).grid(row=9,column=2)
e2=Entry(root,bd=3,textvariable=e21)
e2.grid(row=8,column=3)

Label(root,text="Death cases",font=("Serif",10,"bold")).grid(row=10,column=2)
Label(root,text="",font=("Serif",6,"bold")).grid(row=11,column=2)
e3=Entry(root,bd=3,textvariable=e31)
e3.grid(row=10,column=3)

Label(root,text="Confirmed cases",font=("Serif",10,"bold")).grid(row=12,column=2)
Label(root,text="",font=("Serif",6,"bold")).grid(row=13,column=2)
e4=Entry(root,bd=3,textvariable=e41)
e4.grid(row=12,column=3)

Label(root,text="Recovered cases",font=("Serif",10,"bold")).grid(row=14,column=2)
Label(root,text="",font=("Serif",6,"bold")).grid(row=15,column=2)
e5=Entry(root,bd=3,textvariable=e51)
e5.grid(row=14,column=3)

Label(root,text="",font=("Serif",6,"bold")).grid(row=16,column=2)
Button(root,text="Show data",font=("Serif",10,"bold"),command=show_data,bg="lightgreen").grid(row=17,column=3,sticky=W,pady=4)
Button(root,text=" Show Countries",font=("Serif",10,"bold"),command=show_countries,bg="lightgreen").grid(row=17,column=2,sticky=W,pady=4)
Button(root,text="Exit",font=("Serif",10,"bold"),command=exit,width=10,bg="lightgreen").grid(row=18,column=3,pady=4,sticky=W)
Button(root,text="Clear",font=("Serif",10,"bold"),command=clear,width=10,bg="lightgreen").grid(row=18,column=2,pady=4,sticky=W)


root.mainloop()