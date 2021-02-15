from tkinter import *
from PIL import ImageTk,Image
import imdb

root = Tk()
root.geometry("1500x800+0+0")
root.title("Movie description generator")
root.config(bg='black')

img1 = ImageTk.PhotoImage(Image.open('background.jpg'))
lbl_bg = Label(root,image=img1,bg='black')
lbl_bg.place(x=0,y=0)

frame1 = Frame(root,height=600,width=500,bd=6,relief=RIDGE,bg='white')
frame1.place(x=800,y=130)

lbl_name = Label(frame1,text='Movie Name',font=('fixedsys',16),bg = 'white')
lbl_name.place(x=10,y=20)
name=StringVar()
entry_name = Entry(frame1,font=('fixedsys',14),bg = 'white',width=17,textvariable=name)
entry_name.place(x=170,y=25)

lbl_year = Label(frame1,text='Year Released',font=('fixedsys',16),bg = 'white')
lbl_year.place(x=10,y=73)
year = StringVar()
entry_year = Entry(frame1,font=('fixedsys',14),bg = 'white',width=17,textvariable=year)
entry_year.place(x=170,y=75)

lbl_genres = Label(frame1,text='Genres',font=('fixedsys',16),bg = 'white')
lbl_genres.place(x=10,y=123)
genres = StringVar()
entry_genres = Entry(frame1,font=('fixedsys',14),bg = 'white',width=17,textvariable=genres)
entry_genres.place(x=170,y=125)

lbl_language = Label(frame1,text='Language',font=('fixedsys',16),bg = 'white')
lbl_language.place(x=10,y=173)
language = StringVar()
entry_language = Entry(frame1,font=('fixedsys',14),bg = 'white',width=17,textvariable=language)
entry_language.place(x=170,y=175)

lbl_box_office = Label(frame1,text='Budget',font=('fixedsys',16),bg = 'white')
lbl_box_office.place(x=10,y=223)
budget = StringVar()
entry_box_office = Entry(frame1,font=('fixedsys',14),bg = 'white',width=17,textvariable=budget)
entry_box_office.place(x=170,y=225)

lbl_Rating = Label(frame1,text='Rating',font=('fixedsys',16),bg = 'white')
lbl_Rating.place(x=10,y=273)
rating = StringVar()
entry_Rating = Entry(frame1,font=('fixedsys',14),bg = 'white',width=17,textvariable=rating)
entry_Rating.place(x=170,y=275)

lbl_cast = Label(frame1,text='Cast',font=('fixedsys',16),bg = 'white')
lbl_cast.place(x=10,y=323)
text_cast = Text(frame1,font=('fixedsys',12),bg = 'white',height=10,width=30)
text_cast.place(x=170,y=325)

def enter():
    data = imdb.IMDb()
    movie_name = name.get()
    movies = data.search_movie(movie_name)
    index = movies[0].getID()
    movie = data.get_movie(index)
    keys = movie.keys()
    ans_cast = movie['cast']
    list_of_cast = ','.join(map(str, ans_cast))

    if 'year' not in keys:
        year.set("")
    else:
        ans_year = movie['year']
        year.set(ans_year)
    if 'languages' not in keys:
        language.set("")
    else:
        ans_language = movie['languages']
        language.set(ans_language)
    if 'rating' not in keys:
        rating.set("")
    else:
        ans_rating = movie['rating']
        rating.set(ans_rating)
    if 'genres' not in keys:
        genres.set("")
    else:
        ans_genres = movie['genres']
        genres.set(ans_genres)
    if 'box office' not in keys:
        budget.set("")
    else:
        ans_box_office = movie['box office']
        budget.set(ans_box_office)

    text_cast.insert(END,list_of_cast)


def clear():
    name.set("")
    year.set("")
    genres.set("")
    language.set("")
    budget.set("")
    rating.set("")
    text_cast.delete('1.0',END)

btn_enter = Button(frame1,text='Enter',font=('fixedsys',14),bg = 'white',command=enter)
btn_enter.place(x=370,y=20)
btn_clear = Button(frame1,text='Clear',font=('fixedsys',14),bg = 'white',command=clear)
btn_clear.place(x=370,y=495)

root.mainloop()
