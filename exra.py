
from tkinter import *

root = Tk()
import tkinter.messagebox as tmsg

root.geometry("500x500")
root.title("FRIENDSHIP FORM")
root.configure(background="pink")


def son():
    with open("asdfg.text", "a") as k:
        k.write(
            f"\nNAME={var.get()}\nCONTACT NO.={var2.get()}\nE mail ID={var3.get()}\nSTATE={c.get()}\nDISTRIC={var32.get()}\nBRANCH={varr.get()}")
    tmsg.showinfo("SUBMITTED!", f"welcome {var.get()} ji \n THANK YOU SIR...")


l0 = Label(root, text="BEST FRIEND", font="comicsansms,bold,20", fg="red")
l0.place(x=200, y=10)

l1 = Label(root, text="ENTER NAME=", width=20, font=("bold", 10), bg="pink")
l1.place(x=20, y=53)
var = StringVar()
e1 = Entry(root, textvariable=var)
e1.place(x=200, y=53)

l12 = Label(root, text="CONTACT NO.=", width=20, font=("bold", 10), bg="pink")
l12.place(x=20, y=83)
var2 = StringVar()
e12 = Entry(root, textvariable=var2)
e12.place(x=200, y=83)

l13 = Label(root, text="E mail ID=", width=20, font=("bold", 10), bg="pink")
l13.place(x=20, y=113)
var3 = StringVar()
e13 = Entry(root, textvariable=var3)
e13.place(x=200, y=113)

l12 = Label(root, text="STATE =", width=20, font=("bold", 10), bg="pink")

l12.place(x=20, y=143)

list = ["rajasthan"]
list1 = ["bihar"]
list2 = ["delhi"]

c = StringVar()
droplist = OptionMenu(root, c, list, list1, list2)
droplist.config(width=15)
c.set("select your state")
droplist.place(x=200, y=143)

l13 = Label(root, text="DESTRIC=", width=20, font=("bold", 10), bg="pink")
l13.place(x=20, y=173)
var32 = StringVar()
e13 = Entry(root, textvariable=var32)
e13.place(x=200, y=173)

l1l = Label(root, text="BRANCH=", width=20, font=("bold", 10), bg="pink")
l1l.place(x=20, y=200)
varr = StringVar()

ss2 = Entry(root, textvariable=varr)
ss2.place(x=200, y=200)

b1 = Button(root, text="SUBMIT", width=10, font="conicsansms", fg="red", command=son)
b1.place(x=220, y=230)

root.mainloop()

