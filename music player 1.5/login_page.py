from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql as mk
#functions    



def forgot_pass():
    def change_password():
        if usename.get()=='' or passwodd=='' or cpasswor.get()=='':
            messagebox.showerror('error','all fields required',parent=window)
        elif cpasswor.get()!=passwodd.get():
            messagebox.showerror('error','password missmatch',parent=window)
        else:
            con=mk.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor()
            query='use userdata'
            mycursor.execute(query)
            query='select * from data where username=%s'
            mycursor.execute(query,(usename.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('error','incorrect username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(passwodd.get(),usename.get()))
                con.commit()
                con.close()
                messagebox.showinfo('done','changed password')
                window.destroy()
    def cpas_enter(event):
        if cpasswor.get()=='conform password':
            cpasswor.delete(0,END)
    def use_enter(event):
        if usename.get()=='enter username':
            usename.delete(0,END)

    def pas_enter(event):
        if passwodd.get()=='enter new password':
            passwodd.delete(0,END)

    window=Toplevel()
    window.title='forgot password'
    window.geometry('300x400+350+100')
    window.resizable(False,False)
    window.config(bg='#ACA8A5')
    head=Label(window,text='RESET PASSWORD',font=('robot',15))
    head.place(x=50,y=70)
    
    usename=Entry(window,width=25,font=('ariel',11),fg='grey',bg='light grey')
    usename.insert(0,'enter username')
    usename.place(x=50,y=140)

    usename.bind('<FocusIn>',use_enter)

    passwodd=Entry(window,width=25,font=('ariel',11),fg='grey',bg='light grey')
    passwodd.insert(0,'enter new password')
    passwodd.place(x=50,y=200)

    passwodd.bind('<FocusIn>',pas_enter)

    cpasswor=Entry(window,width=25,font=('ariel',11),fg='grey',bg='light grey')
    cpasswor.insert(0,'conform password')
    cpasswor.place(x=50,y=260)

    cpasswor.bind('<FocusIn>',cpas_enter)

    subbtn=Button(window,text='SUBMIT',bg='light grey',command=change_password,width=13,bd=False,activeforeground='white',activebackground='#ACA8A5',font=('century',18,'bold'))
    subbtn.place(x=50,y=300)

    window.mainloop()



    

def login_user():
    if username.get()=='' or passwordd.get()=='':
        messagebox.showerror('ERROR','invalid username or password')
    else:
        try:
            con=mk.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor()
        except:
            messagebox.showerror('error','connectivity problem')
            return
        
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(username.get(),passwordd.get()))
        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror('error','user not found')
        else:
            messagebox.showinfo('welcome','successfully logged in')
            login.destroy()
            import music_player

            
            



def signup_page():
    login.destroy()
    import signup


def show():
    closeeye.config(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\closedeye.png')
    passwordd.config(show='*')
    eyebtn.config(command=hide)


def hide():
    closeeye.config(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\openeye.png')
    passwordd.config(show='')
    eyebtn.config(command=show)

def user_enter(event):
    if username.get()=='enter username':
        username.delete(0,END)

def pass_enter(event):
    if passwordd.get()=='enter password':
        passwordd.delete(0,END)
        passwordd.config(show='*')
 
#main#
login=Tk()
login.title('MUSIC BOX')
login.geometry('800x600+250+50')

login.resizable(False,False)
bg=ImageTk.PhotoImage(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\MUSIC BX (1).jpg')
bglabel=Label(login,image=bg)
bglabel.place(x=0,y=0)
heading=Label(login,text='USER LOGIN',font=('Helvetica',18),bg='grey',fg='white')
heading.place(x=250,y=100)
username=Entry(login,width=25,font=('ariel',11),fg='white',bg='grey')
username.insert(0,'enter username')
username.place(x=250,y=160)

username.bind('<FocusIn>',user_enter)

passwordd=Entry(login,width=25,font=('ariel',11),fg='white',bg='grey')
passwordd.insert(0,'enter password')
passwordd.place(x=250,y=220)


passwordd.bind('<FocusIn>',pass_enter)

closeeye=PhotoImage(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\closedeye.png')
eyebtn=Button(login,image=closeeye,cursor='hand2',command=show)
eyebtn.place(x=435,y=223)

forgotbtn=Button(login,text='forgot password?',command=forgot_pass,bg='grey',cursor='hand2',activeforeground='white',activebackground='#ACA8A5',bd=False)
forgotbtn.place(x=355,y=255)

loginbtn=Button(login,text='LOGIN',command=login_user,bg='grey',bd=False,activeforeground='white',activebackground='#ACA8A5',font=('century',8,'bold'))
loginbtn.place(x=250,y=255)

flab=Label(login,text='-------------------or-------------------',bg='#ACA8A5',fg='white',font=('Helvetica',15))
flab.place(x=245,y=300)


llab=Label(login,text='LOGIN THROUGH SOCIAL MEDIA:',bg='#ACA8A5',fg='white',font=('Helvetica',13))
llab.place(x=260,y=340)

goggle=PhotoImage(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\google.png')
goglab=Label(login,image=goggle,bg='#ACA8A5')
goglab.place(x=290,y=395)

face=PhotoImage(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\facebook.png')
facelab=Label(login,image=face,bg='#ACA8A5')
facelab.place(x=350,y=395)

twit=PhotoImage(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\twitter.png')
twitlab=Label(login,image=twit,bg='#ACA8A5')
twitlab.place(x=420,y=395)

ulab=Label(login,text='Dont Have A Account?',bg='#ACA8A5',fg='white',font=('Helvetica',9,'bold'))
ulab.place(x=260,y=450)

creatbtn=Button(login,text='create account',bg='#ACA8A5',fg='blue',bd=False,cursor='hand2',command=signup_page,activeforeground='grey',activebackground='#ACA8A5',font=('century',9,'bold underline'))
creatbtn.place(x=400,y=450)

login.mainloop()