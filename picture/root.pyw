from tkinter import *
from PIL import ImageTk, Image
root=Tk()
w = 600
h = 400
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw-w)/2
y = (sh-h)/2-50
root.geometry(('%dx%d+%d+%d') % (w, h, x, y))
image=Image.open("C:\\Users\\mws83\\Desktop\\tkinter\\project\\ana.png")
bck=ImageTk.PhotoImage(image)
lbl=Label(root,image=bck)
lbl.place(x=-2,y=-2)
root.overrideredirect(True)
def delete():
    root.destroy()
root.after(4000,delete)
root.mainloop()