from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql as mk
#functions
def clear():
    emaill.delete(0,END)
    username.delete(0,END)
    passwordd.delete(0,END)
    cpassword.delete(0,END)
    check.set(0)

def con_database():
    if emaill.get()=='' or username.get()=='' or passwordd.get()=='' or cpassword.get=='':
        messagebox.showerror('ERROR','all fields are required')
    elif passwordd.get() != cpassword.get():
        messagebox.showerror('ERROR','password missmatch')
    elif check.get()==0:
        messagebox.showerror('ERROR','plz agree to the terms')
    else:
        try:
            con=mk.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor()
            con.commit()
            
        except:
            messagebox.showerror('ERROR','database connectivity issue')
            return
        
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
            
            query='select * from data where email=%s'
            mycursor.execute(query,(emaill.get()))
            row=mycursor.fetchone()
            if row !=None:
                messagebox.showerror('error','email id is taken')
            else:
                query='select * from data where  username=%s'
                mycursor.execute(query,(username.get()))
                row=mycursor.fetchone()
                if row !=None:
                    messagebox.showerror('error','username already exist')
                    return
                else:

                    query='insert into data(email,username,password) values(%s,%s,%s)'
                    mycursor.execute(query,(emaill.get(),username.get(),passwordd.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('SUCCESS','registered')
                    clear()
                    loginn_page()
        
                  

       
def loginn_page():
    signup.destroy()
    import login_page

def user_enter(event):
    if username.get()=='enter username':
        username.delete(0,END)

def pass_enter(event):
    if passwordd.get()=='enter password':
        passwordd.delete(0,END)

def cpass_enter(event):
    if cpassword.get()=='conform password':
        cpassword.delete(0,END)

def email_enter(event):
    if emaill.get()=='enter email ID here':
        emaill.delete(0,END)

signup=Tk()
signup.title('MUSIC BOX')
signup.geometry('800x600+250+50')

bg=ImageTk.PhotoImage(file='C:\\Users\\japhy\\OneDrive\\Desktop\\music player 1.5\\MUSIC BX .jpg')
bglabel=Label(signup,image=bg)
bglabel.place(x=0,y=0)
heading=Label(signup,text='SIGN UP - create account',font=('Helvetica',18),bg='#ACA8A5',fg='white')
heading.place(x=250,y=100)

emaill=Entry(signup,width=25,font=('ariel',11),fg='white',bg='grey')
emaill.insert(0,'enter email ID here')
emaill.place(x=250,y=190)

emaill.bind('<FocusIn>',email_enter)

username=Entry(signup,width=25,font=('ariel',11),fg='white',bg='grey')
username.insert(0,'enter username')
username.place(x=250,y=260)

username.bind('<FocusIn>',user_enter)

passwordd=Entry(signup,width=25,font=('ariel',11),fg='white',bg='grey')
passwordd.insert(0,'enter password')
passwordd.place(x=250,y=330)

passwordd.bind('<FocusIn>',pass_enter)

cpassword=Entry(signup,width=25,font=('ariel',11),fg='white',bg='grey')
cpassword.insert(0,'conform password')
cpassword.place(x=250,y=400)

cpassword.bind('<FocusIn>',cpass_enter)

check=IntVar()
tnc=Checkbutton(signup,text='Agree to the terms and condition',bg='#ACA8A5',bd=False,variable=check,activebackground='#ACA8A5',font=('helvetica',8,'bold'))
tnc.place(x=250,y=430)

signupbtn=Button(signup,text='SIGN UP',bg='#ACA8A5',activeforeground='white',command=con_database,activebackground='#ACA8A5',width=28,font=('open sans',10,'bold'))
signupbtn.place(x=250,y=460)

ulab=Label(signup,text='already Have A Account?',bg='#ACA8A5',fg='white',font=('Helvetica',9,'bold'))
ulab.place(x=260,y=500)

loginbtn=Button(signup,text='log in',bg='#ACA8A5',fg='blue',bd=False,cursor='hand2',command=loginn_page,activeforeground='grey',activebackground='#ACA8A5',font=('century',9,'bold underline'))
loginbtn.place(x=410,y=500)

signup.mainloop()