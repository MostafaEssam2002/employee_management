from email import message
from tkinter import * 
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk, Image
# def editemployee():
def editemployee():
    image=Image.open("C:\\Users\\mws83\\Desktop\\tkinter\\project\\wesley-tingey-mvLyHPRGLCs-unsplash.jpg")
    frm=Tk()
    conn = mysql.connector.connect(host=sv1.get(),user=sv2.get(),password=sv3.get(),database=sv3.get())
    # conn = mysql.connector.connect(host="localhost",user="usr",password="123456789",database="hr")
    mycursor = conn.cursor()
    frm.geometry("600x400")
    frm.title("Edit Employee")
    frm.resizable(False,False)
    frm.iconbitmap("C:\\Users\\mws83\\Desktop\\tkinter\\project\\All_logo32-xp.ico")
    sv30=StringVar()
    fnt = ("consolas", 20)
    bck=ImageTk.PhotoImage(image)
    lbl=Label(frm,image=bck)
    lbl.place(x=0,y=0) 
    lbl1=Label(frm,text="Enter Employee ID",font=fnt,bg="#513FAB",fg="navy")
    lbl1.pack(fill=X)
    e1=Entry(frm,textvariable=sv30,fg="navy",font=fnt)
    e1.pack(padx=10,pady=10)
    photo2=PhotoImage(file='C:\\Users\\mws83\\Desktop\\tkinter\\project\\et.png').subsample(4,4)
    sv30.set("140")
    def frm5():
        frm5 = Toplevel()
        frm5.config(background="#222435")
        frm5.title('add employee')
        w = 1120
        h = 660
        sw = frm5.winfo_screenwidth()
        sh = frm5.winfo_screenheight()
        x = (sw-w)/2#+100  # 183
        y = (sh-h)/2-100
        frm5.geometry(('%dx%d+%d+%d') % (w, h, x, y))
        frm5.iconbitmap("C:\\Users\\mws83\\Desktop\\tkinter\\project\\All_logo32-xp.ico")
        fnt = ("consolas", 20)
        pad = 10
        sv5 = StringVar()
        sv6 = StringVar()
        sv7 = StringVar()
        sv8 = StringVar()
        sv9 = StringVar()
        sv10 = StringVar()
        sv11 = StringVar()
        sv12 = StringVar()
        sv13 = StringVar()
        sv14 = StringVar()
        sv15 = StringVar()
        mycursor.execute("select EMPLOYEE_ID from EMPLOYEES WHERE EMPLOYEE_ID='%s'" %(sv30.get()))
        rows=(mycursor.fetchall())
        mycursor.execute("select FIRST_NAME from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r1=(mycursor.fetchall())
        mycursor.execute("select LAST_NAME from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r2=(mycursor.fetchall())
        mycursor.execute("select EMAIL from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r3=(mycursor.fetchall())
        mycursor.execute("select PHONE_NUMBER from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r4=(mycursor.fetchall())
        mycursor.execute("select HIRE_DATE from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r5=(mycursor.fetchall())
        mycursor.execute("select JOB_ID from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r6=(mycursor.fetchall())
        mycursor.execute("select SALARY from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r7=(mycursor.fetchall())
        mycursor.execute("select COMMISSION_PCT from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r8=(mycursor.fetchall())
        mycursor.execute("select MANAGER_ID from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r9=(mycursor.fetchall())
        mycursor.execute("select DEPARTMENT_ID from EMPLOYEES WHERE EMPLOYEE_ID='%s'"%(sv30.get()))
        r10=(mycursor.fetchall())
        total=mycursor.rowcount
        sv5.set(rows)
        sv6.set(r1)
        sv7.set(r2)
        sv8.set(r3)
        sv9.set(r4)
        sv10.set(r5)
        sv11.set(r6)
        sv12.set(r7)
        sv13.set(r8)
        sv14.set(r9)
        sv15.set(r10)
        def num(text):
            if str.isdigit(text):
                return True
            else:
                return False
        fun = frm5.register(num)
        l1 = Label(frm5, text="employee id", bg="#222435", fg="#44f005", font=fnt).grid(row=0, column=0, padx=10, pady=10)
        e1 = Entry(frm5, textvariable=sv5, background="#222435", font=fnt,foreground="#44f005", validate='key', validatecommand=(fun, '%P'))
        e1.grid(row=1, column=0, padx=pad, pady=pad)
        e1.focus()
        l2 = Label(frm5, text="first name", bg="#222435", fg="#44f005", font=fnt).grid(row=0, column=1, padx=10, pady=10)
        e2 = Entry(frm5, textvariable=sv6, bg="#222435",font=fnt, foreground="#44f005")
        e2.grid(row=1, column=1, padx=pad, pady=pad)
        l3 = Label(frm5, text="last number", bg="#222435", fg="#44f005", font=fnt).grid(row=0, column=2, padx=10, pady=10)
        e3 = Entry(frm5, textvariable=sv7, bg="#222435",font=fnt, foreground="#44f005")
        e3.grid(row=1, column=2, padx=pad, pady=pad)
        hr = Label(frm5, text="===========================================================================================================================================",bg="#222435", fg="#44f005").grid(row=2, column=0, columnspan=3)
        l4 = Label(frm5, text="Email", bg="#222435", fg="#44f005",font=fnt).grid(row=3, column=0, padx=10, pady=10)
        e4 = Entry(frm5, textvariable=sv8, bg="#222435",font=fnt, foreground="#44f005")
        e4.grid(row=4, column=0, padx=pad, pady=pad)
        l5 = Label(frm5, text="phone number", bg="#222435", fg="#44f005", font=fnt).grid(row=3, column=1, padx=10, pady=10)
        e5 = Entry(frm5, textvariable=sv9, bg="#222435",font=fnt, foreground="#44f005")
        e5.grid(row=4, column=1, padx=pad, pady=pad)
        l6 = Label(frm5, text="bir date", bg="#222435", fg="#44f005", font=fnt).grid(row=3, column=2, padx=10, pady=10)
        e6 = Entry(frm5, textvariable=sv10, bg="#222435",font=fnt, foreground="#44f005")
        e6.grid(row=4, column=2, padx=pad, pady=pad)
        hr = Label(frm5, text="===========================================================================================================================================",bg="#222435", fg="#44f005").grid(row=5, column=0, columnspan=3)
        l7 = Label(frm5, text="jop id", bg="#222435", fg="#44f005",font=fnt).grid(row=6, column=0, padx=10, pady=10)
        e7 = Entry(frm5, textvariable=sv11, bg="#222435",font=fnt, foreground="#44f005")
        e7.grid(row=7, column=0, padx=pad, pady=pad)
        l8 = Label(frm5, text="salary", bg="#222435", fg="#44f005",font=fnt).grid(row=6, column=1, padx=10, pady=10)
        e8 = Entry(frm5, textvariable=sv12, bg="#222435",font=fnt, foreground="#44f005")
        e8.grid(row=7, column=1, padx=pad, pady=pad)
        l9 = Label(frm5, text="COMMISSION_PCT", bg="#222435", fg="#44f005", font=fnt).grid(row=6, column=2, padx=10, pady=10)
        e9 = Entry(frm5, textvariable=sv13, bg="#222435",font=fnt, foreground="#44f005")
        e9.grid(row=7, column=2, padx=pad, pady=pad)
        hr = Label(frm5, text="===========================================================================================================================================",bg="#222435", fg="#44f005").grid(row=8, column=0, columnspan=3)
        l10 = Label(frm5, text="manager_id", bg="#222435", fg="#44f005", font=fnt).grid(row=9, column=0, padx=10, pady=10)
        e10 = Entry(frm5, textvariable=sv14, bg="#222435",font=fnt, foreground="#44f005")
        e10.grid(row=10, column=0, padx=pad, pady=pad)
        l11 = Label(frm5, text="department_id)", bg="#222435", fg="#44f005", font=fnt).grid(row=9, column=1, padx=10, pady=10)
        e11 = Entry(frm5, textvariable=sv15, bg="#222435",font=fnt, foreground="#44f005")
        e11.grid(row=10, column=1, padx=pad, pady=pad)
        hr = Label(frm5, text="===========================================================================================================================================",bg="#222435", fg="#44f005").grid(row=11, column=0, columnspan=3)
        def save():
            mycursor.execute("UPDATE EMPLOYEES SET FIRST_NAME = '%s' WHERE EMPLOYEE_ID='%s'"%(sv6.get(),sv30.get()))
            # mycursor.execute("UPDATE EMPLOYEES SET FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE = '%s' WHERE EMPLOYEE_ID='%s'"%(sv6.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET LAST_NAME = '%s' WHERE EMPLOYEE_ID='%s'"%(sv7.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET EMAIL = '%s' WHERE EMPLOYEE_ID='%s'"%(sv8.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET PHONE_NUMBER = '%s' WHERE EMPLOYEE_ID='%s'"%(sv9.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET HIRE_DATE = '%s' WHERE EMPLOYEE_ID='%s'"%(sv10.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET JOB_ID = '%s' WHERE EMPLOYEE_ID='%s'"%(sv11.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET SALARY = '%s' WHERE EMPLOYEE_ID='%s'"%(sv12.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET COMMISSION_PCT = '%s' WHERE EMPLOYEE_ID='%s'"%(sv13.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET MANAGER_ID = '%s' WHERE EMPLOYEE_ID='%s'"%(sv14.get(),sv30.get()))
            mycursor.execute("UPDATE EMPLOYEES SET DEPARTMENT_ID = '%s' WHERE EMPLOYEE_ID='%s'"%(sv15.get(),sv30.get()))
            total=mycursor.rowcount
            messagebox.showinfo("edit","Data Has Been Changed")
            frm5.destroy()
        def msg():
            messagebox.showinfo('exit', 'are you sure')
            if True:
                frm5.destroy()
        bt1 = Button(frm5, text="save", bg="blue",command=save,cursor="hand2", font=fnt).grid(row=10, column=2)
        btn = Button(frm5, text="exit", image=photo2,cursor="hand2",height=100,bg="#00C27A", command=msg, font=fnt).grid(row=12, column=1, padx=pad, pady=4)
        frm5.mainloop()
    btn=Button(frm,text="search",command=frm5,font=fnt,cursor="hand2").pack()
    photo2=PhotoImage(file='C:\\Users\\mws83\\Desktop\\tkinter\\project\\et.png').subsample(4,4)
    def ex():
        frm.destroy()
    btn2=Button(frm,text="exit",image=photo2,border="0",bg="#00C27A",command=ex,cursor="hand2",height=90).pack(padx=10,pady=10)
    frm.mainloop()
    conn.commit()