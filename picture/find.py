from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from tkinter import IntVar,Scrollbar,StringVar
import mysql.connector
def find_employee():
    conn = mysql.connector.connect(host='localhost',user='usr',password='123456789',database='hr')
    cursor=conn.cursor()
    frm3=Tk()
    frm3.configure(background='silver')
    sv250=StringVar()
    sv26=StringVar()
    sv27=StringVar()
    pad=10
    fnt=("consolas",20)
    w=860
    h=538
    sw=frm3.winfo_screenwidth()
    sh=frm3.winfo_screenheight()
    x=(sw-w)/2#+180 #183
    y=(sh-h)/2-100#+108
    image=Image.open("C:\\Users\\mws83\\Desktop\\tkinter\\project\\serbg.jpg")
    bck=ImageTk.PhotoImage(image)
    lbl=Label(frm3,image=bck)
    lbl.place(x=0,y=0)
    frm3.geometry(('%dx%d+%d+%d')%(w,h,x,y))
    l1=Label(frm3,text="enter id",bg="lightyellow",fg="blue",font=fnt).place(x="12",y="12")
    e1=ttk.Entry(frm3,textvariable=sv250,font=fnt,width=20,foreground="blue")
    e1.place(x="144",y="12")
    sv250.set('')
    l2=Label(frm3,font=fnt,text="Find more than one employee",fg="navy",bg="#46B6E8",border="0")
    l2.place(x="55",y="95")
    l3=Label(frm3,text="Id Between",font=fnt,bg="#46B6E8",border="0")
    l3.place(x="12",y="192")
    e2=Entry(frm3,font=fnt,width=6,fg="navy",textvariable=sv26)
    e2.place(x="175",y="192")
    l3=Label(frm3,font=fnt,text="AND",fg="navy",border="0")
    l3.place(x="280",y="192")
    e3=Entry(frm3,font=fnt,width=6,textvariable=sv27)
    e3.place(x="340",y="192")
    def search():
        if sv250.get() == " ":
            messagebox.showerror('error', 'enter id')
            e1.focus()
        else:
            frm5 =Toplevel()
            frm5.geometry('1975x100')
            vs=Scrollbar(frm5,width=20,bg="yellow")
            vs.pack(side=RIGHT,fill=Y)
            hs=Scrollbar(frm5,orient='horizontal',width=20,bg="yellow")
            hs.pack(side=BOTTOM,fill=X)
            frm5.title("Employee Data")
            frm5.iconbitmap("C:\\Users\\mws83\\Desktop\\tkinter\\project\\filetable_120155.ico")
            style=ttk.Style()
            style.theme_use("alt")
            style.configure("Treeview",font="Verdana 14",background="silver",foreground="navy",rowheight=25,fieldbackground="silver")
            mytree=ttk.Treeview(frm5,style="Treeview",height="300")
            #define column
            mytree['columns']=("EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "EMAIL", "PHONE_NUMBER", "HIRE_DATE", "JOB_ID", "SALARY", "COMMISSION_PCT", "MANAGER_ID", "DEPARTMENT_ID")
            #foramt
            mytree.column("#1",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#0",width=0,minwidth=0,anchor=CENTER)
            mytree.column("#2",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#3",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#4",width=350,minwidth=25,anchor=CENTER)
            mytree.column("#5",width=240,minwidth=25,anchor=CENTER)
            mytree.column("#6",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#7",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#8",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#9",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#10",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#11",width=170,minwidth=25,anchor=CENTER)
            #heading
            mytree.heading("#1",text="EMPLOYEE_ID",anchor=W)
            mytree.heading("#2",text="FIRST_NAME",anchor=W)
            mytree.heading("#3",text="LAST_NAME",anchor=W)
            mytree.heading("#4",text="EMAIL",anchor=W)
            mytree.heading("#5",text="PHONE_NUMBER",anchor=W)
            mytree.heading("#6",text="HIRE_DATE",anchor=W)
            mytree.heading("#7",text="JOB_ID",anchor=W)
            mytree.heading("#8",text="SALARY",anchor=W)
            mytree.heading("#9",text="COMMISSION_PCT",anchor=W)
            mytree.heading("#10",text="MANAGER_ID",anchor=W)
            mytree.heading("#11",text="DEPARTMENT_ID",anchor=W)
            #insert data
            conn = mysql.connector.connect(host='localhost',user='usr',password='123456789',database='hr')
            cursor=conn.cursor()
            cursor.execute("select * from employees WHERE EMPLOYEE_ID='%s'" %(sv250.get()))
            # cursor.execute("SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID ='%s';"%(sv250))
            r1=(cursor.fetchall())
            for i in r1:
                mytree.insert('','end',values=(i))
            mytree.pack(side=TOP,fill=X)
            vs.config(command=mytree.yview)
            hs.config(command=mytree.xview)
            frm5.mainloop()
    def search_2():
        if sv26.get() == " ":
            messagebox.showerror('error', 'enter id')
            e1.focus()
        elif sv27.get() == " ":
            messagebox.showerror("error","enter id")
        else:
            frm4 =Toplevel()
            frm4.geometry('1000x800')
            vs=Scrollbar(frm4,width=20,bg="yellow")
            vs.pack(side=RIGHT,fill=Y)
            hs=Scrollbar(frm4,orient='horizontal',width=20,bg="yellow")
            hs.pack(side=BOTTOM,fill=X)
            frm4.title("Employees Data")
            frm4.iconbitmap("C:\\Users\\mws83\\Desktop\\tkinter\\project\\filetable_120155.ico")
            style=ttk.Style()
            style.theme_use("alt")
            style.configure("Treeview",font="Verdana 14",background="silver",foreground="navy",rowheight=25,fieldbackground="silver")
            mytree=ttk.Treeview(frm4,style="Treeview",height="300")
            #define column
            mytree['columns']=("EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "EMAIL", "PHONE_NUMBER", "HIRE_DATE", "JOB_ID", "SALARY", "COMMISSION_PCT", "MANAGER_ID", "DEPARTMENT_ID")
            #foramt
            mytree.column("#1",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#0",width=0,minwidth=0,anchor=CENTER)
            mytree.column("#2",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#3",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#4",width=350,minwidth=25,anchor=CENTER)
            mytree.column("#5",width=240,minwidth=25,anchor=CENTER)
            mytree.column("#6",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#7",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#8",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#9",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#10",width=170,minwidth=25,anchor=CENTER)
            mytree.column("#11",width=170,minwidth=25,anchor=CENTER)
            #heading
            mytree.heading("#1",text="EMPLOYEE_ID",anchor=W)
            mytree.heading("#2",text="FIRST_NAME",anchor=W)
            mytree.heading("#3",text="LAST_NAME",anchor=W)
            mytree.heading("#4",text="EMAIL",anchor=W)
            mytree.heading("#5",text="PHONE_NUMBER",anchor=W)
            mytree.heading("#6",text="HIRE_DATE",anchor=W)
            mytree.heading("#7",text="JOB_ID",anchor=W)
            mytree.heading("#8",text="SALARY",anchor=W)
            mytree.heading("#9",text="COMMISSION_PCT",anchor=W)
            mytree.heading("#10",text="MANAGER_ID",anchor=W)
            mytree.heading("#11",text="DEPARTMENT_ID",anchor=W)
            #insert data
            conn = mysql.connector.connect(host='localhost',user='usr',password='123456789',database='hr')
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID BETWEEN '%s' AND '%s'"%(sv26.get(),sv27.get()))
            r1=(cursor.fetchall())
            for i in r1:
                mytree.insert('','end',values=(i))
            mytree.pack(side=TOP,fill=X)
            vs.config(command=mytree.yview)
            hs.config(command=mytree.xview)
            frm4.mainloop()
    photo=PhotoImage(file="C:\\Users\\mws83\\Desktop\\tkinter\\project\\rch.png").subsample(5,5)
    btn=Button(frm3,font=fnt,command=search,text='search',height="52",width='111',relief="flat",border="0",image=photo,cursor="watch",bg='#46B6E8')
    btn.place(x="460",y="6")
    photo10=PhotoImage(file="C:\\Users\\mws83\\Desktop\\tkinter\\project\\ser2.png").subsample(2,2)
    bt1=Button(frm3,text="",height=55,width=50,command=search_2,bg="#00A8F3",image=photo10,relief="flat",border="0")
    bt1.place(x="440",y="182")
    photo1=PhotoImage(file="C:\\Users\\mws83\\Desktop\\tkinter\\project\\e1.png").subsample(2,2)
    def ee():
        frm3.iconify()
    bt0=Button(frm3,text="exit",height=102,width=99,image=photo1,border="0",command=exit,bg="#46B6E8")
    bt0.place(x="380",y="282")

    conn.commit()
    frm3.mainloop()
find_employee()
