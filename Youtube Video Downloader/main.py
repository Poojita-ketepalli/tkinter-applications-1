from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pytube
from pytube import YouTube
import time
import os

root=Tk()
root.title("Youtube Video downloader")
root.geometry("400x400")
root.config(bg="#FFB99A")

def download():
    link = link_entry.get("1.0","end-1c")

    if link == '':
        messagebox.showerror("YouTube Downloader", "Please paste a link here")
    else:
        try:
            yt = pytube.YouTube(link)
            SAVE_PATH = "E:/"
            stream = yt.streams.first()
            time.sleep(2)
            link_entry.delete(1.0, 'end')
            link_entry.insert('end', 'Wait Downloading ......')
            time.sleep(5)
            stream.download(SAVE_PATH)
            messagebox.showinfo("YouTube Downloader", 'Video has been download successfully')
            link_entry.delete(1.0, 'end')
        except:
            messagebox.showerror("YouTube Downloader", "Connection error")

img=ImageTk.PhotoImage(Image.open("youtube.png"))
img_label=Label(root,image=img,bg="#FFB99A")
img_label.place(x=170,y=50)

link_label=Label(root,text="Link",bg="#FFB99A",font=("serif",12,"bold"))
link_label.place(x=30,y=160)

link_entry=Text(root,font=("serif",12,"bold"),width=27,height=2)
link_entry.place(x=80,y=150)

Download_button=Button(root,text="Download",font=("serif",12,"bold"),bg="red",fg="white",command=download)
Download_button.place(x=150,y=220)



root.mainloop()
