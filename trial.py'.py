from tkinter import *
from tkinter import messagebox

day=Tk()
day.geometry("1000x1500")
def Multiplication():
    num1=23
    num2=46
    answer=num1*num2
    msg=messagebox.showinfo("Simple Multiplication",f"{num1}*{num2}={answer}")
myButton=Button(day,text="Show Answer",command=MultiplicationTable)
myButton.place(x=300, y=600)
day.mainloop()
