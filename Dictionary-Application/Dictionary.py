from tkinter import *
from PIL import Image,ImageTk
from PyDictionary import PyDictionary

root=Tk()
root.title("Dictionary Application")
root.geometry("600x600")
root.config(bg="#8eaa9e")

def meaning():
    word_get=word.get()
    dictionary=PyDictionary()
    answer=dictionary.meaning(word_get)
    meaning_text.insert('end',answer)
def synonym():
    word_get = word.get()
    dictionary = PyDictionary()
    answer = dictionary.synonym(word_get)
    meaning_text.insert('end', answer)
def antonym():
    word_get = word.get()
    dictionary = PyDictionary()
    answer = dictionary.antonym(word_get)
    meaning_text.insert('end', answer)
def clear():
    word.set("")
    meaning_text.delete(1.0,'end')

img=ImageTk.PhotoImage(Image.open("dictionary.png"))
img_label=Label(root,image=img,bg="#8eaa9e")
img_label.place(x=230,y=10)

word_label=Label(root,text="Word",font=("Arial",13,"bold"),fg="#ffe37a",bg="#8eaa9e")
word_label.place(x=100,y=170)
word=StringVar()
word_entry=Entry(root,textvariable=word,font=("Arial",13,"bold"),bd=4,bg="gray80")
word_entry.place(x=170,y=170)

meaning_text=Text(root,width=40,height=8,bg="gray80",bd=4)
meaning_text.place(x=100,y=220)

meaning_button=Button(root,text="Meaning",font=("Arial",13,"bold"),bg="#ff7c8f",fg="white",command=meaning)
meaning_button.place(x=70,y=420)

synonym_button=Button(root,text="Synonym",font=("Arial",13,"bold"),bg="#ff7c8f",fg="white",command=synonym)
synonym_button.place(x=180,y=420)

antonym_button=Button(root,text="Antonym",font=("Arial",13,"bold"),bg="#ff7c8f",fg="white",command=antonym)
antonym_button.place(x=300,y=420)

clear_button=Button(root,text="Clear",font=("Arial",13,"bold"),bg="#ff7c8f",fg="white",command=clear)
clear_button.place(x=420,y=420)

exit_button=Button(root,text="Exit",font=("Arial",13,"bold"),bg="#ff7c8f",fg="white",command=exit)
exit_button.place(x=500,y=420)



root.mainloop()
