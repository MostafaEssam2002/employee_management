from tkinter import *
import mysql.connector
from tkinter import Tk, ttk, Toplevel
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button 
n=1
def connect():   
        frm = Toplevel()
        w = 600
        h = 400
        sw = frm.winfo_screenwidth()
        sh = frm.winfo_screenheight()
        x = (sw-w)/2
        y = (sh-h)/2
        frm.geometry(('%dx%d+%d+%d') % (w, h, x, y))
        sv1 = StringVar()
        sv2 = StringVar()
        sv3 = StringVar()
        sv4 = StringVar()
        p = 10
        frm.resizable(False,False)
        frm.iconbitmap("C:\\Users\\mws83\\Desktop\\tkinter\\project\\sql\\chain.ico")
        fnt = ("consolas", 20)
        frm.config(background='#262626')
        frm.title("mysql connector")
        l1 = Label(frm, text="host name", fg="#00ff00", bg="#262626",font=fnt).grid(row=0, column=0, padx=p, pady=p)
        e1 = Entry(frm, textvariable=sv1, font=fnt, background="#262626", fg="#00ff00")
        e1.grid(row=0, column=1)
        l2 = Label(frm, text="user name", fg="#00ff00", bg="#262626",font=fnt).grid(row=1, column=0, padx=p, pady=p)
        e2 = Entry(frm, textvariable=sv2, font=fnt, bg="#262626", fg="#00ff00")
        e2.grid(row=1, column=1)
        l3 = Label(frm, text="password", fg="#00ff00", bg="#262626",font=fnt).grid(row=2, column=0, padx=p, pady=p)
        e3 = Entry(frm, textvariable=sv3, font=fnt, bg="#262626", fg="#00ff00")
        e3.grid(row=2, column=1)
        e3.config(show="*")
        #--------------++++++++++++++++++++++-----------------+++++++++++-------------
        photo1=PhotoImage(file='C:\\Users\mws83\Downloads\show.png').subsample(14,14)
        photo2=PhotoImage(file='C:\\Users\mws83\Downloads\hide.png').subsample(14,14)
        photo3=PhotoImage(file='C:\\Users\\mws83\\Desktop\\tkinter\\project\\exit2.png').subsample(1,1)
        
        global n
        # n=1
        def click():
                # n=1
                global n
                # n=1
                if n==1:
                        e3.config(show="")
                        btn.config(image=photo2)
                        n=2
                else:
                        e3.config(show="*")
                        btn.config(image=photo1)
                        n=1
                #262626
                # frm.destroy()
        btn=Button(frm,command=click,bg="wheat",image=photo1,cursor='hand2',border='0')
        btn.grid(row=2,column=2)
        # btn.place(x=500,y=122)
        #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-2+-+--++++++++++++++++++++++++++++++++++++
        l4 = Label(frm, text="database name", fg="#00ff00", bg="#262626",font=fnt).grid(row=3, column=0, padx=p, pady=p)
        e4 = Entry(frm, textvariable=sv4, font=fnt, bg="#262626", fg="#00ff00")
        e4.grid(row=3, column=1)
        sv1.set('localhost')
        sv2.set('usr')
        sv3.set('123456789')
        sv4.set('hr')
        def connection():
                conn = mysql.connector.connect(
                                host=sv1.get(),
                                user=sv2.get(),
                                password=sv3.get(),
                                database=sv4.get()
                        )
                mycursor = conn.cursor()

        def con():
                if sv1.get() == '':
                        messagebox.showerror('error', 'enter host')
                        e1.focus()
                elif sv2.get() == '':
                        messagebox.showerror('error', 'enter user name')
                        e2.focus()
                elif sv3.get() == '':
                        messagebox.showerror('error', 'enter password')
                        e3.focus()
                elif sv4.get() == '':
                        messagebox.showerror('error', 'enter database')
                        e4.focus()
                else:
                        connection()
                        frm.destroy()
        bt = Button(frm, text="connect", font=fnt, command=con, fg="black",background="#00ff00").grid(row=4, column=1, padx=p, pady=p)
        # e3.bind("<Return>",con())
        def destroy():
                frm.destroy()
        c = Button(frm, text="  exit ",image=photo3,width=80,height=95, border=0,command=destroy, font=fnt, fg="black",bg="#262626").grid(row=5, column=1, padx=p, pady=0)
        frm.mainloop()
# connect()
