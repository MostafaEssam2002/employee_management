from multiprocessing.managers import Token
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
frm2 = Tk()
frm2.config(background="#222435")
frm2.title('add employee')
w = 1120
h = 660
sw = frm2.winfo_screenwidth()
sh = frm2.winfo_screenheight()
x = (sw-w)/2#+100  # 183
y = (sh-h)/2-100
# frm2.overrideredirect(True)
frm2.geometry(('%dx%d+%d+%d') % (w, h, x, y))
# frm2.geometry('1356x640')
# image=Image.open("C:\\Users\\mws83\\Desktop\\tkinter\\project\\mos.jpg")
# bck=ImageTk.PhotoImage(image)
# lbl=Label(frm2,image=bck)
# lbl.place(x=0,y=0)
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
def num(text):
    if str.isdigit(text):
        return True
    else:
        return False
fun = frm2.register(num)
l1 = Label(frm2, text="employee id", bg="#222435", fg="#44f005", font=fnt).grid(
    row=0, column=0, padx=10, pady=10)
e1 = Entry(frm2, textvariable=sv5, background="#222435", font=fnt,
            foreground="#44f005", validate='key', validatecommand=(fun, '%P'))
e1.grid(row=1, column=0, padx=pad, pady=pad)
e1.focus()
l2 = Label(frm2, text="first name", bg="#222435", fg="#44f005", font=fnt).grid(
    row=0, column=1, padx=10, pady=10)
e2 = Entry(frm2, textvariable=sv6, bg="#222435",
            font=fnt, foreground="#44f005")
e2.grid(row=1, column=1, padx=pad, pady=pad)
l3 = Label(frm2, text="last number", bg="#222435", fg="#44f005", font=fnt).grid(
    row=0, column=2, padx=10, pady=10)
e3 = Entry(frm2, textvariable=sv7, bg="#222435",
            font=fnt, foreground="#44f005")
e3.grid(row=1, column=2, padx=pad, pady=pad)
hr = Label(frm2, text="===========================================================================================================================================",
            bg="#222435", fg="#44f005").grid(row=2, column=0, columnspan=3)
l4 = Label(frm2, text="Email", bg="#222435", fg="#44f005",
            font=fnt).grid(row=3, column=0, padx=10, pady=10)
e4 = Entry(frm2, textvariable=sv8, bg="#222435",
            font=fnt, foreground="#44f005")
e4.grid(row=4, column=0, padx=pad, pady=pad)
l5 = Label(frm2, text="phone number", bg="#222435", fg="#44f005", font=fnt).grid(
    row=3, column=1, padx=10, pady=10)
e5 = Entry(frm2, textvariable=sv9, bg="#222435",
            font=fnt, foreground="#44f005")
e5.grid(row=4, column=1, padx=pad, pady=pad)
l6 = Label(frm2, text="bir date", bg="#222435", fg="#44f005", font=fnt).grid(
    row=3, column=2, padx=10, pady=10)
e6 = Entry(frm2, textvariable=sv10, bg="#222435",
            font=fnt, foreground="#44f005")
e6.grid(row=4, column=2, padx=pad, pady=pad)
hr = Label(frm2, text="===========================================================================================================================================",
            bg="#222435", fg="#44f005").grid(row=5, column=0, columnspan=3)
l7 = Label(frm2, text="jop id", bg="#222435", fg="#44f005",
            font=fnt).grid(row=6, column=0, padx=10, pady=10)
e7 = Entry(frm2, textvariable=sv11, bg="#222435",
            font=fnt, foreground="#44f005")
e7.grid(row=7, column=0, padx=pad, pady=pad)
l8 = Label(frm2, text="salary", bg="#222435", fg="#44f005",
            font=fnt).grid(row=6, column=1, padx=10, pady=10)
e8 = Entry(frm2, textvariable=sv12, bg="#222435",
            font=fnt, foreground="#44f005")
e8.grid(row=7, column=1, padx=pad, pady=pad)
l9 = Label(frm2, text="COMMISSION_PCT", bg="#222435", fg="#44f005", font=fnt).grid(
    row=6, column=2, padx=10, pady=10)
e9 = Entry(frm2, textvariable=sv13, bg="#222435",
            font=fnt, foreground="#44f005")
e9.grid(row=7, column=2, padx=pad, pady=pad)
hr = Label(frm2, text="===========================================================================================================================================",
            bg="#222435", fg="#44f005").grid(row=8, column=0, columnspan=3)
l10 = Label(frm2, text="manager_id", bg="#222435", fg="#44f005", font=fnt).grid(
    row=9, column=0, padx=10, pady=10)
e10 = Entry(frm2, textvariable=sv14, bg="#222435",
            font=fnt, foreground="#44f005")
e10.grid(row=10, column=0, padx=pad, pady=pad)
l11 = Label(frm2, text="department_id)", bg="#222435", fg="#44f005", font=fnt).grid(
    row=9, column=1, padx=10, pady=10)
e11 = Entry(frm2, textvariable=sv15, bg="#222435",
            font=fnt, foreground="#44f005")
e11.grid(row=10, column=1, padx=pad, pady=pad)
hr = Label(frm2, text="===========================================================================================================================================",
            bg="#222435", fg="#44f005").grid(row=11, column=0, columnspan=3)
sv5.set('')
sv15.set('')
sv14.set('')
sv13.set('')
sv12.set('')
def save():
    if sv5.get() == "":
        messagebox.showerror('error', 'enter id')
        e1.focus()
    elif sv6.get() == '':
        messagebox.showerror('error', 'enter first name')
        e2.focus()
    elif sv7.get() == '':
        messagebox.showerror('error', 'enter last name')
        e3.focus()
    elif sv8.get() == '':
        messagebox.showerror('error', 'enter email')
        e4.focus()
    elif sv9.get() == '':
        messagebox.showerror('error', 'enter phone number')
        e5.focus()
    elif sv10.get() == '':
        messagebox.showerror('error', 'enter hir_date')
        e6.focus()
    elif sv11.get() == '':
        messagebox.showerror('error', 'enter jop id')
        e7.focus()
    elif sv12.get() == 0:
        messagebox.showerror('error', 'enter salary')
        e8.focus()
    elif sv13.get() == 0:
        messagebox.showerror('error', 'enter commision_pct')
        e9.focus()
    elif sv14.get() == 0:
        messagebox.showerror('error', 'enter manager id')
        e10.focus()
    elif sv15.get() == 0:
        messagebox.showerror('error', 'enter department id')
        e11.focus()
    else:
        def connection():
            conn = mysql.connector.connect(
                host="localhost",
                user="usr",
                password="123456789",
                database="h"
            )
            mycursor = conn.cursor()
            # def crept1():
            txt200=[str(sv5.get())]
            cipher_list=[]
            for i in txt200:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            a=''.join(cipher_list)
            print(a)
            # crept1()
        # def crept2():
            txt60=[str(sv6.get())]
            cipher_list=[]
            for i in txt60:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            b=''.join(cipher_list)
            print(b)
            # crept2(            def crept3():
            txt77=[str(sv6.get())]
            cipher_list=[]
            for i in txt77:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            c=''.join(cipher_list)
            print(c)
            # crept3()
            # def crept4():
            txt88=[str(sv7.get())]
            cipher_list=[]
            for i in txt88:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            d=''.join(cipher_list)
            print(d)
            # crept4()
            # def crept5():
            txt99=[str(sv8.get())]
            cipher_list=[]
            for i in txt99:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            e=''.join(cipher_list)
            print(e)
            # crept5()
            # def crept6():
            txt110=[str(sv9.get())]
            cipher_list=[]
            for i in txt110:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            f=''.join(cipher_list)
            print(f)
            # crept6()
            # def crept7():
            txt220=[str(sv10.get())]
            cipher_list=[]
            for i in txt220:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            g=''.join(cipher_list)
            print(g)
        # crept7()
            # def crept8():
            txt330=[str(sv11.get())]
            cipher_list=[]
            for i in txt330:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            h=''.join(cipher_list)
            print(h)
            # crept8()
            # def crept9():
            txt440=[str(sv12.get())]
            cipher_list=[]
            for i in txt440:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            i=''.join(cipher_list)
            print(i)
            # crept9()
            # def crept10():
            txt550=[str(sv13.get())]
            cipher_list=[]
            for i in txt550:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            k=''.join(cipher_list)
            print(k)
            # crept10()
            # def crept11():
            txt660=[str(sv14.get())]
            cipher_list=[]
            for i in txt660:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            l=''.join(cipher_list)
            print(l)
            # crept11()
            # def crept11():
            txt770=[str(sv15.get())]
            cipher_list=[]
            for i in txt770:
                position=ord(i)
                new_letter=chr((position+5))
                cipher_list.append(new_letter)
            m=''.join(cipher_list)
            print(m)
            mycursor.execute("""INSERT INTO employees VALUES( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (a,b,c,d,e,f,g,h,i,k,l,m))
            conn.commit()
        connection()
        sv5.set('')
        sv6.set('')
        sv7.set('')
        sv8.set('')
        sv9.set('')
        sv10.set('')
        sv11.set('')
        sv12.set('')
        sv13.set('')
        sv14.set('')
        sv15.set('')
        e1.focus()
def msg():
    messagebox.showinfo('exit', 'are you sure')
    if True:
        frm2.destroy()
photo2=PhotoImage(file='C:\\Users\\mws83\\Desktop\\tkinter\\project\\sql\\picture\\sve.png').subsample(4,4)
bt1 = Button(frm2, text="save",bg="#222435",command=save,width="140",border=0,height="65",image=photo2,font=fnt)
bt1.place(x=770,y=450)
mophoto=PhotoImage(file='C:\\Users\\mws83\\Desktop\\tkinter\\project\\sql\\picture\\mo.png').subsample(4,4)
btn = Button(frm2, text="exit", bg="#222435", command=msg,image=mophoto,width="110",border=0,height="110",font=fnt)
btn.place(x=500,y=540)
frm2.iconbitmap("C:\\Users\\mws83\\Desktop\\tkinter\\project\\sql\\picture\\addemplouee.ico")
frm2.mainloop()
