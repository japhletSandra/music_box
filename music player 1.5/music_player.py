import os
import threading
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from mutagen.mp3 import MP3
from PIL import ImageTk
from pygame import mixer



#function


def downloade():
    root.destroy()
    import downloader

def start_count(t):
    global paused
    
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = ' - ' + timeformat
            time.sleep(1)
            current_time += 1



def show_details(play_song):
    file_data = os.path.splitext(play_song)
    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = ' - ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


#function button\

def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            
            show_details(play_it)
        except:
            messagebox.showerror('File not found', 'could not find the file. Please check again.')



def stop_music():
    mixer.music.stop()
    


paused = FALSE


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    
def rewind_music():
    play_music()



def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

    mixer.music.queue(filename_path)

playlist=[]

def add_to_playlist(filename):
    
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1



def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)
    stop_music()

def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

muted = FALSE

def mute_music():
    global muted
    if muted:  # Unmute the music
        mixer.music.set_volume(0.7)
        volumeBtn.configure(text='VOLUME ON')
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(text='MUTED')
        scale.set(0)
        muted = TRUE  



root=Tk()
root.title('music box')
root.resizable(False,False)
root.geometry('600x400+350+100')

mixer.init()

root.config(bg='#737373')

menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)





menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)






subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="menu", menu=subMenu)
subMenu.add_command(label="mp3 download from youtube",command=downloade)
subMenu.add_command(label="Recommend me songs - comming soon")
subMenu.add_command(label="Recommend me songs (based on emotion)- comming soon")
imgicon=PhotoImage(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\images\\bg.png')
imgl=Label(root,image=imgicon,bg='#737373')
imgl.place(x=0,y=0)

#playlist frame
rightframe = Frame(root)
rightframe.place(x=240, y=150,width=350,height=240)

playlistbox = Listbox(rightframe,bg='black',fg='white')
playlistbox.place(x=0,y=0,width=350,height=200)



addBtn =Button(rightframe, text="+ Add",font=('robot',10), command=browse_file)
addBtn.place(x=5,y=210,width=100)




delBtn =Button(rightframe, text="- Del",font=('robot',10), command=del_song)
delBtn.place(x=245,y=210,width=100)




#functions

#buttons
playbtn=Button(root,text='PLAY',command=play_music,font=('century',13))
playbtn.place(x=10,y=230)

pausebtn=Button(root,text='PAUSE',command=pause_music,font=('century',13))
pausebtn.place(x=120,y=230)

stopbtn=Button(root,text='STOP',command=stop_music,font=('century',13))
stopbtn.place(x=66,y=230)

rewindbtn=Button(root,text='REWIND',command=rewind_music,font=('century',13))
rewindbtn.place(x=5,y=270)


lengthlabel =Label(root, text='--:--',bg='#737373',bd=False)
lengthlabel.place(x=250,y=135,height=10)

currenttimelabel =Label(root, text='--:--',bg='#737373',bd=False, relief=GROOVE)
currenttimelabel.place(x=290,y=135,height=10)

volumeBtn =Button(root, text='VOLUME ON',font=('century',13), command=mute_music)
volumeBtn.place(x=88, y=270)

scale =Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
scale.place(x=5,y=310)



def on_closing():
    stop_music()
    root.destroy()

root.mainloop()