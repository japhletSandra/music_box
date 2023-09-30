import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
import os
import webbrowser

def destroy():
    ytl.destroy()
    import music_player
def Widgets():
 
    head_label = Label(ytl, text="YT MP3 DOWNLOAD",padx=15,pady=15,font="SegoeUI 14",fg="indigo")
    head_label.grid(row=1,column=1,padx=50,pady=5)
 
    link_label = Label(ytl,text="YouTube link :",bg="light grey",pady=5,padx=5)
    link_label.grid(row=2,column=0,pady=5,padx=5)
 
    ytl.linkText = Entry(ytl,width=35,textvariable=video_Link,font="Arial 14")
    ytl.linkText.grid(row=2,column=1,pady=5,padx=5,columnspan=2)
 
 
    destination_label = Label(ytl,text="Destination :",bg="light grey",pady=5,padx=9)
    destination_label.grid(row=3,column=0,pady=5,padx=5)
 
 
    ytl.destinationText = Entry(ytl,width=27,textvariable=download_Path,font="Arial 14")
    ytl.destinationText.grid(row=3,column=1,pady=5,padx=5)
 
 
    browse_B = Button(ytl,text="Browse",command=Browse,width=10,bg="bisque",relief=GROOVE)
    browse_B.grid(row=3,column=2,pady=1,padx=1)
 
    Download_B = Button(ytl,text="Download mp3",command=Download,width=20,fg='white',bg="indigo",pady=10,padx=15,relief=GROOVE,font="Georgia, 13")
    Download_B.grid(row=4,column=1,pady=20,padx=20)
 
 
def open_browser():
    webbrowser.open_new('https://www.youtube.com/')


def Browse():

    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory) 
 
 #functions
def Download():

    Youtube_link = video_Link.get()

    download_Folder = download_Path.get()
 
    getVideo = YouTube(Youtube_link)

    videoStream = getVideo.streams.filter(only_audio=True).first()

    out_file = videoStream.download(output_path=download_Folder)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
   
    messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_Folder)
    destroy()
 
ytl=Tk()
ytl.title('MUSIC BOX')
ytl.geometry('520x280+500+100')
bg='light grey'
video_Link = StringVar()
download_Path = StringVar() 

searchbtn=Button(text='search yt',font='century',command=open_browser)
searchbtn.place(x=10,y=170)
# Calling the Widgets() function
Widgets()

ytl.mainloop()

