from tkinter import *
from tkinter import messagebox

sh=Tk()
sh.geometry("1000x1500")
def Table():
    """:arg"""
    mylist=[]
    for i in range(1,12):
        for j in range(1,12):
            check=f"{i}*{j}= {i*j}"
            mylist.append(check)
    msg=messagebox.showinfo("Multiplication Table",f"{mylist}")
B=Button(sh,text="Show results",command=Table)
B.place(x=100,y=100)
sh.mainloop()