from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800")
root.title("RESTAURANT MANAGEMENT SYSTEM")

text_input=StringVar()

tops = Frame(root,width =1600,height=50,relief=RAISED,bd=8)
tops.pack(side=TOP)
label1 = Label(tops,font=('arial',50,'bold'),text="RESTAURANT BILLING SYSTEM",fg="black",bd=10,anchor=W)
label1.grid(row=0,column=0)

f1 = Frame(root,width =900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width =300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

label1 = Label(tops,font=('arial',20,'bold'),text=localtime,fg="blue",bd=10,anchor=W)
label1.grid(row=1,column=0)

#===========================================CALCULATOR==================================================================================
def btn_click(item):
    global expression
    expression = expression + str(item)
    text_input.set(expression)
def btn_clear():
    global expression
    expression = ""
    text_input.set("")
def btn_equal():
    global expression
    result=str(eval(expression)) #eval function evaluates the string expressio directly
    text_input.set(result)
expression = ""

textdisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg='powder blue',justify='right')
textdisplay.grid(columnspan=5)

_1 = Button(f2, text='1', fg='black', bg='powder blue',command=lambda: btn_click(1), height=2, width=5,font=('arial bold',20),bd=8)
_1.grid(row=2, column=0)
_2 = Button(f2, text='2', fg='black', bg='powder blue',command=lambda: btn_click(2), height=2, width=5,font=('arial bold',20),bd=8)
_2.grid(row=2, column=1)
_3 = Button(f2, text='3', fg='black', bg='powder blue',command=lambda: btn_click(3), height=2, width=5,font=('arial bold',20),bd=8)
_3.grid(row=2, column=2)
_4 = Button(f2, text='4', fg='black', bg='powder blue',command=lambda: btn_click(4), height=2, width=5,font=('arial bold',20),bd=8)
_4.grid(row=3, column=0)
_5 = Button(f2, text='5', fg='black', bg='powder blue',command=lambda: btn_click(5), height=2, width=5,font=('arial bold',20),bd=8)
_5.grid(row=3, column=1)
_6 = Button(f2, text='6', fg='black', bg='powder blue',command=lambda: btn_click(6), height=2, width=5,font=('arial bold',20),bd=8)
_6.grid(row=3, column=2)
_7 = Button(f2, text='7', fg='black', bg='powder blue',command=lambda: btn_click(7), height=2, width=5,font=('arial bold',20),bd=8)
_7.grid(row=4, column=0)
_8 = Button(f2, text='8', fg='black', bg='powder blue', command=lambda: btn_click(8), height=2, width=5,font=('arial bold',20),bd=8)
_8.grid(row=4, column=1)
_9 = Button(f2, text='9', fg='black', bg='powder blue',command=lambda: btn_click(9), height=2, width=5,font=('arial bold',20),bd=8)
_9.grid(row=4, column=2)
_0 = Button(f2, text='0', fg='black', bg='powder blue', command=lambda: btn_click(0), height=2, width=5,font=('arial bold',20),bd=8)
_0.grid(row=5, column=0)
plus = Button(f2, text='+', fg='black', bg='powder blue',command=lambda: btn_click('+'), height=2, width=5,font=('arial bold',20),bd=8)
plus.grid(row=2, column=3)
minus = Button(f2, text='-', fg='black', bg='powder blue',command=lambda: btn_click('-'), height=2, width=5,font=('arial bold',20),bd=8)
minus.grid(row=3, column=3)
multiply = Button(f2, text='*', fg='black', bg='powder blue',command=lambda:btn_click('*'), height=2, width=5,font=('arial bold',20),bd=8)
multiply.grid(row=4, column=3)
divide = Button(f2, text='/', fg='black', bg='powder blue', command=lambda:btn_click('/'), height=2, width=5,font=('arial bold',20),bd=8)
divide.grid(row=5, column=3)
equal = Button(f2, text='=', fg='black', bg='powder blue', command=btn_equal, height=2, width=5,font=('arial bold',20),bd=8)
equal.grid(row=5, column=2)
clear = Button(f2, text='Clear', fg='black', bg='powder blue',command=btn_clear, height=2, width=5,font=('arial bold',20),bd=8)
clear.grid(row=5, column=1)

#=====================================================================================================================================
txtreference=StringVar()
reference=Label(f1, text='Reference',font=('arial bold',12),bd=8)
reference.grid(row=0, column=0)
textreference=Entry(f1,textvariable=txtreference,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textreference.grid(row=0, column=1)

txtbajji=StringVar()
bajji=Label(f1, text='Bajji',font=('arial bold',12),bd=8)
bajji.grid(row=1, column=0)
textbajji=Entry(f1,textvariable=txtbajji,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textbajji.grid(row=1, column=1)

txtpunugulu=StringVar()
punugulu=Label(f1, text='Punugulu',font=('arial bold',12),bd=8)
punugulu.grid(row=2, column=0)
textpunugulu=Entry(f1,textvariable=txtpunugulu,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textpunugulu.grid(row=2, column=1)

txtdosa=StringVar()
dosa=Label(f1, text='Dosa',font=('arial bold',12),bd=8)
dosa.grid(row=3, column=0)
textdosa=Entry(f1,textvariable=txtdosa,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textdosa.grid(row=3, column=1)

txtparota=StringVar()
parota=Label(f1, text='Parota',font=('arial bold',12),bd=8)
parota.grid(row=4, column=0)
textparota=Entry(f1,textvariable=txtparota,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textparota.grid(row=4, column=1)

txtidli=StringVar()
idli=Label(f1, text='Idli sambar',font=('arial bold',12),bd=8)
idli.grid(row=5, column=0)
textidli=Entry(f1,textvariable=txtidli,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textidli.grid(row=5, column=1)
#==================================================================================================
txtjuice=StringVar()
juice=Label(f1, text='Lemon Juice',font=('arial bold',12),bd=8)
juice.grid(row=0, column=2)
textjuice=Entry(f1,textvariable=txtjuice,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textjuice.grid(row=0, column=3)

txtcoffee=StringVar()
coffee=Label(f1, text='Coffee',font=('arial bold',12),bd=8)
coffee.grid(row=1, column=2)
textcoffee=Entry(f1,textvariable=txtcoffee,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textcoffee.grid(row=1, column=3)

txttea=StringVar()
tea=Label(f1, text='Tea',font=('arial bold',12),bd=8)
tea.grid(row=2, column=2)
texttea=Entry(f1,textvariable=txttea,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
texttea.grid(row=2, column=3)

txtmilkshake=StringVar()
milkshake=Label(f1, text='Milk Shake',font=('arial bold',12),bd=8)
milkshake.grid(row=3, column=2)
textmilkshake=Entry(f1,textvariable=txtmilkshake,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textmilkshake.grid(row=3, column=3)

txtbuttermilk=StringVar()
buttermilk=Label(f1, text='Butter Milk',font=('arial bold',12),bd=8)
buttermilk.grid(row=4, column=2)
textbuttermilk=Entry(f1,textvariable=txtbuttermilk,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textbuttermilk.grid(row=4, column=3)

txtbadammilk=StringVar()
badammilk=Label(f1, text='Badam Milk',font=('arial bold',12),bd=8)
badammilk.grid(row=5, column=2)
textbadammilk=Entry(f1,textvariable=txtbadammilk,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textbadammilk.grid(row=5, column=3)
#================================================================================================================================
txtveg_pulav=StringVar()
veg_pulav=Label(f1, text='Veg Pulav',font=('arial bold',12),bd=8)
veg_pulav.grid(row=0, column=4)
textveg_pulav=Entry(f1,textvariable=txtveg_pulav,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textveg_pulav.grid(row=0, column=5)

txtbiryani=StringVar()
biryani=Label(f1, text='Biryani',font=('arial bold',12),bd=8)
biryani.grid(row=1, column=4)
textbiryani=Entry(f1,textvariable=txtbiryani,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textbiryani.grid(row=1, column=5)

txtfried_rice=StringVar()
fried_rice=Label(f1, text='Fried Rice',font=('arial bold',12),bd=8)
fried_rice.grid(row=2, column=4)
textfried_rice=Entry(f1,textvariable=txtfried_rice,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textfried_rice.grid(row=2, column=5)

txtveg_tadka=StringVar()
veg_tadka=Label(f1, text='Veg Tadka',font=('arial bold',12),bd=8)
veg_tadka.grid(row=3, column=4)
textveg_tadka=Entry(f1,textvariable=txtveg_tadka,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textveg_tadka.grid(row=3, column=5)

txtjeera_rice=StringVar()
jeera_rice=Label(f1, text='Jeera Rice',font=('arial bold',12),bd=8)
jeera_rice.grid(row=4, column=4)
textjeera_rice=Entry(f1,textvariable=txtjeera_rice,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textjeera_rice.grid(row=4, column=5)

txtlemon_rice=StringVar()
lemon_rice=Label(f1, text='Lemon Rice',font=('arial bold',12),bd=8)
lemon_rice.grid(row=5, column=4)
textlemon_rice=Entry(f1,textvariable=txtlemon_rice,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textlemon_rice.grid(row=5, column=5)
#================================================================================================================================
txtmeal=StringVar()
meal=Label(f1, text='Meal cost',font=('arial bold',12),bd=8)
meal.grid(row=7, column=4)
textmeal=Entry(f1,textvariable=txtmeal,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textmeal.grid(row=7, column=5)

txtservice_charge=StringVar()
service_charge=Label(f1, text='Service charge',font=('arial bold',12),bd=8)
service_charge.grid(row=8, column=4)
textservice_charge=Entry(f1,textvariable=txtservice_charge,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
textservice_charge.grid(row=8, column=5)

txttotal_cost=StringVar()
total_cost=Label(f1, text='Total cost',font=('arial bold',12),bd=8)
total_cost.grid(row=9, column=4)
texttotal_cost=Entry(f1,textvariable=txttotal_cost,font=('arial bold',12),bd=8,
               insertwidth=4,bg='powder blue',justify='right')
texttotal_cost.grid(row=9, column=5)
#================================================================================================================================
def ref():
    x=random.randint(10000,100000)
    y=str(x)
    txtreference.set(y)

    cobajji=float(txtbajji.get())
    copunugulu=float(txtpunugulu.get())
    codosa=float(txtdosa.get())
    coparota=float(txtparota.get())
    coidli=float(txtidli.get())
    cojuice=float(txtjuice.get())
    cocoffee=float(txtcoffee.get())
    cotea=float(txttea.get())
    comilkshake=float(txtmilkshake.get())
    cobuttermilk=float(txtbuttermilk.get())
    cobadammilk=float(txtbadammilk.get())
    copulav=float(txtveg_pulav.get())
    cobiryani=float(txtbiryani.get())
    cotadka=float(txtveg_tadka.get())
    cojeerarice=float(txtjeera_rice.get())
    colemonrice=float(txtlemon_rice.get())
    cofriedrice=float(txtfried_rice.get())

    costofbajji=(cobajji *20)
    costofpunugulu=(copunugulu*20)
    costofdosa=(codosa*25)
    costofparota=(coparota*40)
    costofidli=(coidli*25)
    costofjuice=(cojuice*20)
    costofcoffee=(cocoffee*15)
    costoftea=(cotea*10)
    costofpulav=copulav*75
    costofbiryani=cobiryani*150
    costoftadka=cotadka*170
    costofjeerarice=cojeerarice*120
    costoflemonrice=colemonrice*70
    costoffriedrice=cofriedrice*120
    costofmilkshake=comilkshake*45
    costofbadammilk=cobadammilk*65
    costofbuttermilk=cobuttermilk*25


    costofmeal="Rs",str('%0.2f' % (costofbajji + costofpunugulu + costofdosa + costofparota + costofidli + costofjuice + costofcoffee + costoftea +costofbiryani+costofpulav+costoftadka+costofjeerarice+costoflemonrice+costoffriedrice+costofmilkshake+costofbadammilk+costofbuttermilk))
    totalcost = costofbajji + costofpunugulu + costofdosa + costofparota + costofidli + costofjuice + costofcoffee + costoftea+costofbiryani+costofpulav+costoftadka+costofjeerarice+costoflemonrice+costoffriedrice+costofmilkshake+costofbadammilk+costofbuttermilk
    servicecharge=(costofbajji + costofpunugulu + costofdosa + costofparota + costofidli + costofjuice + costofcoffee + costoftea+costofbiryani+costofpulav+costoftadka+costofjeerarice+costoflemonrice+costoffriedrice+costofmilkshake+costofbadammilk+costofbuttermilk)/99
    overallcost="RS",str('%0.2f' % (totalcost+servicecharge))

    txtmeal.set(costofmeal)
    txtservice_charge.set(servicecharge)
    txttotal_cost.set(overallcost)
    
    Label(f1,text='Thank You for visiting us!!!',font=("arial bold",20),fg='green').grid(row=8,columnspan=5)


def quit():
    root.destroy()
def reset():
    txtreference.set("")
    txtbajji.set("")
    txtpunugulu.set("")
    txtdosa.set("")
    txtparota.set("")
    txtidli.set("")
    txtjuice.set("")
    txtcoffee.set("")
    txttea.set("")
    txtmilkshake.set("")
    txtbadammilk.set("")
    txtbuttermilk.set("")
    txtmeal.set("")
    txtservice_charge.set("")
    txttotal_cost.set("")
    txtveg_pulav.set("")
    txtbiryani.set("")
    txtveg_tadka.set("")
    txtjeera_rice.set("")
    txtlemon_rice.set("")
    txtfried_rice.set("")

def menu():
    screen=Toplevel(root)
    screen.geometry("800x600")
    screen.title("MENU CARD")
    label=Label(screen,text="MENU CARD",font=('arial bold',50),fg='black')
    label.pack()
    menuframe=Frame(screen,width=600,height=400)
    menuframe.pack(side=LEFT)
    label1=Label(menuframe,text="Hey there!!! Look at todays speacials",font=('arialbold',20)).grid(row=0,column=2)

    def breakfast():
        screen1=Toplevel(screen)
        screen1.geometry("800x600")
        screen1.title("Breakfast Menu")
        Label(screen1,text="Breakfast items",font=('arialbold',30),fg='blue').pack()
        label2=Label(screen1, text='Bajji',font=('arial bold',16),bd=8).pack()
        label3=Label(screen1, text='Punugulu',font=('arial bold',16),bd=8).pack()
        label4=Label(screen1, text='idli',font=('arial bold',16),bd=8).pack()
        label5=Label(screen1, text='dosa',font=('arial bold',16),bd=8).pack()
        label6=Label(screen1, text='Parota',font=('arial bold',16),bd=8).pack()
        Label(screen1,text="Have a Nice Day!!!:):):)",font=('arial bold',26),bd=8,fg='green').pack()
    def liquids():
        screen2=Toplevel(screen)
        screen2.geometry("800x600")
        screen2.title("Liquids")
        Label(screen2,text="Liquids",font=('arialbold',30),fg='blue').pack()
        Label(screen2, text='Lemon Juice',font=('arial bold',16),bd=8).pack()
        Label(screen2, text='Milk Shake',font=('arial bold',16),bd=8).pack()
        Label(screen2, text='Butter Milk',font=('arial bold',16),bd=8).pack()
        Label(screen2, text='Badam Milk',font=('arial bold',16),bd=8).pack()
        Label(screen2, text='Coffee',font=('arial bold',16),bd=8).pack()
        Label(screen2, text='Tea',font=('arial bold',16),bd=8).pack()
        Label(screen2,text="Have a Nice Day!!!:):):)",font=('arial bold',26),bd=8,fg='green').pack()
    def rice_items():
        screen3=Toplevel(screen)
        screen3.geometry("800x600")
        screen3.title("Rice items")
        Label(screen3,text="Rice items",font=('arialbold',30),fg='blue').pack()
        Label(screen3, text='Pulav',font=('arial bold',16),bd=8).pack()
        Label(screen3, text='Biryani',font=('arial bold',16),bd=8).pack()
        Label(screen3, text='Fried Rice',font=('arial bold',16),bd=8).pack()
        Label(screen3, text='Lemon Rice',font=('arial bold',16),bd=8).pack()
        Label(screen3, text='Jeera Rice',font=('arial bold',16),bd=8).pack()
        Label(screen3, text='Veg Tadka',font=('arial bold',16),bd=8).pack()
        Label(screen3,text="Have a Nice Day!!!:):):)",font=('arial bold',26),bd=8,fg='green').pack()



    button1=Button(menuframe,fg='black',font=('arial bold',20),
                width=8,text="Breakfast",command=breakfast).grid(row=1,column=2)
    Label(menuframe,text="").grid(row=2,column=2)
    button2=Button(menuframe,fg='black',font=('arial bold',20),
                width=8,text="Liquids",command=liquids).grid(row=3,column=2)
    Label(menuframe,text="").grid(row=4,column=2)
    button3=Button(menuframe,fg='black',font=('arial bold',20),
                width=8,text="Rice items",command=rice_items).grid(row=5,column=2)
    Label(menuframe,text="").grid(row=6,column=2)

btntotal=Button(f1,padx=8,pady=8,fg='black',font=('arial bold',20),relief=FLAT,
                text="Total",command=ref).grid(row=6,column=0)
btnreset=Button(f1,padx=8,pady=8,fg='black',font=('arial bold',20),relief=FLAT,
                text="Reset",command=reset).grid(row=6,column=1)
btnmenu=Button(f1,padx=8,pady=8,fg='black',font=('arial bold',20),relief=FLAT,
                text="Menu",command=menu).grid(row=6,column=2)
btnquit=Button(f1,padx=8,pady=8,fg='black',font=('arial bold',20),relief=FLAT,
                text="Quit",command=quit).grid(row=6,column=3)




root.mainloop()