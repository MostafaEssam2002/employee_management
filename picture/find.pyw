from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from tkinter import IntVar,Scrollbar,StringVar
import mysql.connector
def frm3_4():
    conn = mysql.connector.connect(host='localhost',user='usr',password='123456789',database='hr')
    cursor=conn.cursor()
    frm3=Tk()
    frm3.configure(background='silver')
    sv250=StringVar()
    pad=10
    fnt=("consolas",20)
    w=860
    h=538
    sw=frm3.winfo_screenwidth()
    sh=frm3.winfo_screenheight()
    x=(sw-w)/2#+180 #183
    y=(sh-h)/2-100#+108
    image=Image.open("C:\\Users\\mws83\\Desktop\\tkinter\\project\\bg.jpg")
    bck=ImageTk.PhotoImage(image)
    lbl=Label(frm3,image=bck)
    lbl.place(x=0,y=0)
    frm3.geometry(('%dx%d+%d+%d')%(w,h,x,y))
    l1=Label(frm3,text="enter id",bg="lightyellow",fg="blue",font=fnt).pack(pady=10,padx=10)
    e1=ttk.Entry(frm3,textvariable=sv250,font=fnt,foreground="blue")
    e1.pack(pady=10,padx=10)
    sv250.set('')
    def search():
        if sv250.get() == " ":
            messagebox.showerror('error', 'enter id')
            e1.focus()
        else:
                cursor.execute("select EMPLOYEE_ID from employees WHERE EMPLOYEE_ID='%s'" %(sv250.get()))
                rows=(cursor.fetchall())
                cursor.execute("select FIRST_NAME from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r1=(cursor.fetchall())
                cursor.execute("select LAST_NAME from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r2=(cursor.fetchall())
                cursor.execute("select EMAIL from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r3=(cursor.fetchall())
                cursor.execute("select PHONE_NUMBER from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r4=(cursor.fetchall())
                cursor.execute("select HIRE_DATE from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r5=(cursor.fetchall())
                cursor.execute("select JOB_ID from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r6=(cursor.fetchall())
                cursor.execute("select SALARY from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r7=(cursor.fetchall())
                cursor.execute("select COMMISSION_PCT from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r8=(cursor.fetchall())
                cursor.execute("select MANAGER_ID from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r9=(cursor.fetchall())
                cursor.execute("select DEPARTMENT_ID from employees WHERE EMPLOYEE_ID='%s'"%(sv250.get()))
                r10=(cursor.fetchall())
                total=cursor.rowcount
                #========================================================================================+++++++++++++++++++
                frm4=Toplevel()
                w=1920
                h=1080
                sw=frm4.winfo_screenwidth()
                sh=frm4.winfo_screenheight()
                x=(sw-w)/2+180 #183
                y=(sh-h)/2+99#108
                frm4.geometry(('%dx%d+%d+%d')%(w,h,x,y))
                t=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t.grid(row=0,column=0)
                t1=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t1.grid(row=0,column=1)
                t2=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t2.grid(row=0,column=2)
                t3=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t3.grid(row=0,column=3)
                t4=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t4.grid(row=0,column=4)
                t5=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t5.grid(row=0,column=5)
                t6=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t6.grid(row=0,column=6)
                t7=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t7.grid(row=0,column=7)
                t8=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t8.grid(row=0,column=8)
                t9=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t9.grid(row=0,column=9)
                t10=ttk.Treeview(frm4,columns=(1),show="headings",height="50")
                t10.grid(row=0,column=10)
                t.column("1",width=140)
                t1.column("1",width=140)
                t2.column("1",width=140)
                t3.column("1",width=140)
                t4.column("1",width=140)
                t5.column("1",width=140)
                t6.column("1",width=140)
                t7.column("1",width=140)
                t8.column("1",width=140)
                t9.column("1",width=119)
                t10.column("1",width=140)
                frm4.config(background="lightblue")
                t.heading(1,text="EMPLOYEE_ID")
                t1.heading(1,text="FIRST_NAME")
                t2.heading(1,text="LAST_NAME")
                t3.heading(1,text="EMAIL")
                t4.heading(1,text="PHONE")
                t5.heading(1,text="HIRE_DATE")
                t6.heading(1,text="JOB_ID")
                t7.heading(1,text="SALARY")
                t8.heading(1,text="COMMISSION_PCT")
                t9.heading(1,text="MANAGER_ID")
                t10.heading(1,text="DEPARTMENT_ID")
                for i in rows:
                    t.insert('','end',values=i)
                for i in r1:
                    t1.insert('','end',values=i)
                for i in r2 :
                    t2.insert('','end',values=i)
                for i in r3 :
                    t3.insert('','end',values=i)
                for i in r4 :
                    t4.insert('','end',values=i)
                for i in r5 :
                    t5.insert('','end',values=i)
                for i in r6 :
                    t6.insert('','end',values=i)
                for i in r7 :
                    t7.insert('','end',values=i)
                for i in r8 :
                    t8.insert('','end',values=i)
                for i in r9 :
                    t9.insert('','end',values=i)
                for i in r10 :
                    t10.insert('','end',values=i)
                frm4.mainloop()
    def pr():
        frm3.destroy()
        # print(sv250.get())
    photo=PhotoImage(file="C:\\Users\\mws83\\Desktop\\tkinter\\project\\find.png").subsample(4,4)
    btn=Button(frm3,font=fnt,command=search,text='search',border="0",image=photo,cursor="watch",bg='blue')
    btn.pack(pady=10,padx=10)
    # bt=Button(frm3,text='search',command=search,font=fnt,bg="lightyellow",fg="blue").pack(pady=10,padx=10,column=2,padx=10,pady=10)
    bt=Button(frm3,text='exit',command=pr,font=fnt,bg="lightyellow",fg="blue").pack(pady=10,padx=10)
    conn.commit()
    frm3.mainloop()
frm3_4()
